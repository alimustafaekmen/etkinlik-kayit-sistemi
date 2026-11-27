#!/usr/bin/env python3
"""kanban/tasks.csv'deki kartlardan GitHub Issue'larını ve GitHub Projects panosunu kurar.

Kullanım (proje kökünden; macOS'taki sistem python3'ü yeterli, yalnızca standart kütüphane + gh CLI):
    python3 scripts/setup_kanban.py --dry-run --create-project   # ne yapılacağını göster, GitHub'a yazma
    python3 scripts/setup_kanban.py --create-project             # etiket, milestone, issue ve pano
    python3 scripts/setup_kanban.py --project 3                  # var olan 3 numaralı panoyu kullan

Tekrar çalıştırılabilir: var olan etiket, milestone, issue, pano alanı ve kartlar yeniden oluşturulmaz.
Elle taşınmış kartların Status'u korunur; Status yalnızca boş olan kartlarda CSV'den doldurulur.
"""

from __future__ import annotations

import argparse
import csv
import json
import shlex
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "kanban" / "tasks.csv"
PROJECT_TITLE = "Etkinlik Kayıt Sistemi – Kanban"
PROJECT_DESCRIPTION = "YZM6443 dönem projesi · 5 hafta (23 Kasım – 27 Aralık 2026) · kartlar: kanban/tasks.md"
WEEK10_MONDAY = date(2026, 11, 23)  # dönem haftaları: Hafta 10 … Hafta 14
WEEKS = {"10", "11", "12", "13", "14"}
STATUS_COLORS = {"Todo": "GRAY", "In Progress": "YELLOW", "Issues / Blocked": "RED", "Done": "GREEN"}
WORKFLOWS = ["Software Development", "DevOps & Cloud", "Agile & Sunum"]
NUMBER_FIELD = "Tahmin (saat)"
# İş akışı etiketleri renkli; diğer konu etiketleri (Development, Git, Testing ...) gri
LABEL_COLORS = {"Software Development": "1f6feb", "DevOps & Cloud": "8250df", "Agile & Sunum": "bf8700"}
LABEL_COLORS.update({"Bug": "d73a4a", "Security": "b60205"})
SCOPE_HELP = "gh oturumunda 'project' yetkisi yok. Şunu çalıştırıp tekrar dene:\n  gh auth refresh -s project"

DRY_RUN = False

UPDATE_OPTIONS = """mutation($fieldId: ID!, $options: [ProjectV2SingleSelectFieldOptionInput!]) {
  updateProjectV2Field(input: {fieldId: $fieldId, singleSelectOptions: $options}) { clientMutationId } }"""


def gh(*args: str, write: bool = True, stdin: str | None = None) -> str:
    """gh komutunu çalıştırır. --dry-run'da yazma komutlarını yalnızca yazdırır, okumaları hiç yapmaz."""
    if DRY_RUN:
        if write:
            line = shlex.join(["gh", *args]).replace("\n", "\\n")
            print("  [dry-run]", line if len(line) < 160 else line[:157] + "...")
        return ""
    result = subprocess.run(["gh", *args], text=True, capture_output=True, input=stdin, check=False)
    if result.returncode != 0:
        err = (result.stderr or result.stdout).strip()
        if "scope" in err.lower() and "project" in err.lower():
            sys.exit(SCOPE_HELP)
        raise RuntimeError(f"gh {' '.join(args[:3])} başarısız: {err}")
    return result.stdout.strip()


def gh_json(*args: str, default: object) -> object:
    out = gh(*args, write=False)
    return json.loads(out) if out else default


def load_tasks() -> list[dict]:
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as fh:
        tasks = list(csv.DictReader(fh))
    ids = [t["id"] for t in tasks]
    problems = [f"tekrarlanan id: {i}" for i in set(ids) if ids.count(i) > 1]
    for t in tasks:
        ac = t["acceptance_criteria"].splitlines()
        if t["status"] not in STATUS_COLORS or t["workflow"] not in WORKFLOWS or t["week"] not in WEEKS:
            problems.append(f"{t['id']}: status/workflow/week geçersiz")
        if not 2 <= len(ac) <= 4 or not t["description"] or not t["evidence"]:
            problems.append(f"{t['id']}: Description, 2-4 Acceptance Criteria ve Evidence gerekli")
    if problems:
        sys.exit("tasks.csv hatalı:\n  " + "\n  ".join(problems))
    return tasks


def issue_body(t: dict) -> str:
    box = "x" if t["status"] == "Done" else " "
    ac = "\n".join(f"- [{box}] {line}" for line in t["acceptance_criteria"].splitlines())
    ev = "\n".join(f"- {line}" for line in t["evidence"].splitlines())
    return (
        f"## Task Description\n{t['description']}\n\n## Acceptance Criteria\n{ac}\n\n"
        f"## Evidence\n{ev}\n\n---\n"
        f"*Hafta {t['week']} ({t['week_dates']}) · {t['workflow']} · {t['priority']} · "
        f"{t['estimate_hours']} saat · Branch: `{t['branch']}`*"
    )


def ensure_labels(repo: str, tasks: list[dict]) -> None:
    labels = sorted({name for t in tasks for name in t["labels"].split(";")})
    print(f"Etiketler ({len(labels)})")
    for name in labels:  # --force: varsa rengini günceller, hata vermez
        gh("label", "create", name, "--repo", repo, "--color", LABEL_COLORS.get(name, "ededed"), "--force")


def ensure_milestones(repo: str, tasks: list[dict]) -> None:
    milestones = gh_json("api", f"repos/{repo}/milestones?state=all&per_page=100", default=[])
    existing = {m["title"] for m in milestones}
    weeks = sorted({(int(t["week"]), t["week_dates"]) for t in tasks})
    print(f"Milestone'lar ({len(weeks)})")
    for week, dates in weeks:
        if f"Hafta {week}" in existing:
            continue
        sunday = WEEK10_MONDAY + timedelta(days=7 * (week - 10) + 6)  # pazar 23:59 İstanbul (20:59 UTC)
        fields = [f"title=Hafta {week}", f"description={dates}", f"due_on={sunday}T20:59:59Z"]
        gh("api", f"repos/{repo}/milestones", *(arg for f in fields for arg in ("-f", f)))


def ensure_issues(repo: str, tasks: list[dict]) -> dict[str, str]:
    """Her kart için issue açar (başlık '[ID] ...'). Dönüş: kart id -> issue URL'si."""
    args = ["issue", "list", "--repo", repo, "--state", "all", "--limit", "500", "--json", "title,url,state"]
    listing = gh_json(*args, default=[])
    found = {i["title"].split("]")[0] + "]": i for i in listing if i["title"].startswith("[")}
    urls: dict[str, str] = {}
    created = 0
    print(f"Issue'lar ({len(tasks)})")
    for t in tasks:
        issue = found.get(f"[{t['id']}]")
        if issue is None:
            args = ["issue", "create", "--repo", repo, "--title", f"[{t['id']}] {t['title']}"]
            args += ["--body", issue_body(t), "--milestone", f"Hafta {t['week']}"]
            for label in t["labels"].split(";"):
                args += ["--label", label]
            issue = {"url": gh(*args) or f"<{t['id']} issue URL>", "state": "OPEN"}
            created += 1
        urls[t["id"]] = issue["url"]
        if t["status"] == "Done" and issue["state"] == "OPEN":
            comment = "Tamamlandı. Kanıt:\n" + "\n".join(f"- {e}" for e in t["evidence"].splitlines())
            gh("issue", "close", issue["url"], "--reason", "completed", "--comment", comment)
    print(f"  {created} yeni issue, {len(tasks) - created} zaten vardı")
    return urls


def ensure_project(owner: str, repo: str, number: int | None) -> tuple[str, str]:
    """Panoyu bulur ya da oluşturur, public yapar ve depoya bağlar. Dönüş: (numara, proje id)."""
    if number is None:
        listing = gh_json("project", "list", "--owner", owner, "--format", "json", default={"projects": []})
        number = next((p["number"] for p in listing["projects"] if p["title"] == PROJECT_TITLE), None)
    if number is None:
        out = gh("project", "create", "--owner", owner, "--title", PROJECT_TITLE, "--format", "json")
        number = json.loads(out)["number"] if out else None
    num = str(number or "<N>")
    print(f"Pano #{num}: https://github.com/users/{owner}/projects/{num}")
    settings = ["--visibility", "PUBLIC", "--description", PROJECT_DESCRIPTION]
    gh("project", "edit", num, "--owner", owner, *settings)
    try:
        gh("project", "link", num, "--owner", owner, "--repo", repo.split("/")[1])
    except RuntimeError as exc:
        print(f"  not: depo bağlantısı atlandı (zaten bağlı olabilir): {exc}")
    project_id = gh_json("project", "view", num, "--owner", owner, "--format", "json", default={}).get("id")
    return num, project_id or "<PROJECT_ID>"


def ensure_status_options(field: dict) -> None:
    """Status sütunlarını Todo / In Progress / Issues / Blocked / Done yapar (fazladan seçenekler kalır).

    Seçenekler yeniden yazılınca kartların Status'u boşalabilir; sync_items boş Status'u CSV'den doldurur.
    """
    current = [o["name"] for o in field.get("options", [])]
    missing = [s for s in STATUS_COLORS if s not in current]
    if DRY_RUN:
        print(f"  [dry-run] Status seçenekleri kontrol edilir, eksikler eklenir: {', '.join(STATUS_COLORS)}")
    if not missing or DRY_RUN:
        return
    names = [*STATUS_COLORS, *(n for n in current if n not in STATUS_COLORS)]
    options = [{"name": n, "color": STATUS_COLORS.get(n, "GRAY"), "description": ""} for n in names]
    payload = json.dumps({"query": UPDATE_OPTIONS, "variables": {"fieldId": field["id"], "options": options}})
    try:
        gh("api", "graphql", "--input", "-", stdin=payload)
        print(f"  Status alanına eklendi: {', '.join(missing)}")
    except RuntimeError as exc:
        print(f"  UYARI: {exc}\n  Elle ekle: Pano > ⋯ > Settings > Status > seçenekler: {', '.join(missing)}")


def ensure_fields(num: str, owner: str, tasks: list[dict]) -> dict[str, dict]:
    """Hafta, Alan, Öncelik ve Tahmin alanlarını oluşturur. Dönüş: alan adı -> {id, options: {ad: id}}."""
    wanted = {
        "Hafta": [f"Hafta {w}" for w in sorted({int(t["week"]) for t in tasks})],
        "Alan": WORKFLOWS,
        "Öncelik": sorted({t["priority"] for t in tasks}),
    }
    default = {"fields": [{"id": "<Status>", "name": "Status", "options": []}]}
    listing = gh_json("project", "field-list", num, "--owner", owner, "--format", "json", default=default)
    fields = {f["name"]: f for f in listing["fields"]}
    print("Pano alanları: Status, " + ", ".join([*wanted, NUMBER_FIELD]))
    for name, options in wanted.items():
        if name not in fields:
            kind = ["--data-type", "SINGLE_SELECT", "--single-select-options", ",".join(options)]
            gh("project", "field-create", num, "--owner", owner, "--name", name, *kind)
    if NUMBER_FIELD not in fields:
        gh("project", "field-create", num, "--owner", owner, "--name", NUMBER_FIELD, "--data-type", "NUMBER")
    if "Status" in fields:
        ensure_status_options(fields["Status"])
    if DRY_RUN:
        return {}
    listing = gh_json("project", "field-list", num, "--owner", owner, "--format", "json", default={})
    return {
        f["name"]: {"id": f["id"], "options": {o["name"]: o["id"] for o in f.get("options", [])}}
        for f in listing.get("fields", [])
    }


def sync_items(num: str, owner: str, project_id: str, tasks: list[dict], urls: dict[str, str]) -> None:
    """Issue'ları panoya ekler; Hafta, Alan, Öncelik, Tahmin ve (boşsa) Status'u CSV'den doldurur."""
    fields = ensure_fields(num, owner, tasks)
    args = ["project", "item-list", num, "--owner", owner, "--limit", "500", "--format", "json"]
    listing = gh_json(*args, default={"items": []})
    items = {(i.get("content") or {}).get("url"): i for i in listing["items"]}
    print(f"Pano kartları ({len(tasks)})")
    for t in tasks:
        item = items.get(urls[t["id"]])
        if item is None:
            out = gh("project", "item-add", num, "--owner", owner, "--url", urls[t["id"]], "--format", "json")
            item = json.loads(out) if out else {"id": f"<{t['id']} item>"}
        if DRY_RUN:
            continue
        values = {"Hafta": f"Hafta {t['week']}", "Alan": t["workflow"], "Öncelik": t["priority"]}
        if not item.get("status"):
            values["Status"] = t["status"]
        base = ["project", "item-edit", "--id", item["id"], "--project-id", project_id]
        for name, value in values.items():
            option = fields.get(name, {}).get("options", {}).get(value)
            if option:
                gh(*base, "--field-id", fields[name]["id"], "--single-select-option-id", option)
            else:
                print(f"  UYARI: {t['id']} için '{name}: {value}' seçeneği panoda yok")
        if NUMBER_FIELD in fields:
            gh(*base, "--field-id", fields[NUMBER_FIELD]["id"], "--number", t["estimate_hours"])
    if DRY_RUN:
        print(f"  [dry-run] {len(tasks)} kartın Hafta, Alan, Öncelik, Tahmin ve Status alanları doldurulur")


def main() -> int:
    global DRY_RUN
    parser = argparse.ArgumentParser(description="tasks.csv'den GitHub Issue'ları ve Projects panosunu kurar")
    parser.add_argument("--repo", default="alimustafaekmen/etkinlik-kayit-sistemi")
    parser.add_argument("--dry-run", action="store_true", help="GitHub'a yazmadan planı göster")
    parser.add_argument("--create-project", action="store_true", help="panoyu oluştur (aynı adlıyı kullan)")
    parser.add_argument("--project", type=int, metavar="N", help="var olan N numaralı panoyu kullan")
    args = parser.parse_args()
    DRY_RUN = args.dry_run
    use_project = args.create_project or args.project is not None

    tasks = load_tasks()
    print(f"{len(tasks)} kart okundu: {CSV_PATH.name}" + (" (dry-run: GitHub'a yazılmaz)" if DRY_RUN else ""))
    if not DRY_RUN:
        try:
            status = subprocess.run(["gh", "auth", "status"], text=True, capture_output=True, check=False)
        except FileNotFoundError:
            sys.exit("GitHub CLI (gh) bulunamadı: brew install gh && gh auth login")
        if status.returncode != 0:
            sys.exit("gh oturumu yok. Önce: gh auth login")
        if use_project and "'project'" not in status.stdout + status.stderr:
            sys.exit(SCOPE_HELP)

    ensure_labels(args.repo, tasks)
    ensure_milestones(args.repo, tasks)
    urls = ensure_issues(args.repo, tasks)
    if use_project:
        owner = args.repo.split("/")[0]
        num, project_id = ensure_project(owner, args.repo, args.project)
        sync_items(num, owner, project_id, tasks, urls)
        print("Elle kontrol: Board görünümü (Column by: Status); Workflows: 'Item closed' -> Done")
    print("Tamam.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
