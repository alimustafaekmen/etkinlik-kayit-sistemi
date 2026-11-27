#!/usr/bin/env python3
"""Kanban kartlarını (kanban_gorevleri.csv) GitHub Issues olarak oluşturur ve isteğe bağlı
olarak GitHub Projects panosuna ekler.

Gereksinim: GitHub CLI (https://cli.github.com)  ->  gh auth login
Proje panosu işlemleri için ek yetki:           ->  gh auth refresh -s project

Kullanım:
  # Önce ne yapılacağını görün (hiçbir şey oluşturmaz)
  python3 kanban/github_kanban_kur.py --repo alimustafaekmen/etkinlik-kayit-sistemi --dry-run

  # Etiket, milestone ve issue'ları oluştur
  python3 kanban/github_kanban_kur.py --repo alimustafaekmen/etkinlik-kayit-sistemi

  # Yeni public GitHub Projects panosu oluştur, depoya bağla ve tüm kartları panoya ekle
  python3 kanban/github_kanban_kur.py --repo alimustafaekmen/etkinlik-kayit-sistemi --create-project

  # Mevcut GitHub Projects panosuna (proje numarası URL'de: /users/alimustafaekmen/projects/1) ekle
  python3 kanban/github_kanban_kur.py --repo alimustafaekmen/etkinlik-kayit-sistemi --project 1

Betik tekrar çalıştırılabilir (idempotent): aynı başlıklı issue varsa yeniden oluşturulmaz,
panoda eksikse mevcut panoya eklenir.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

CSV_PATH = Path(__file__).with_name("kanban_gorevleri.csv")

LABEL_COLORS = {
    "Software Development": "1f6feb",
    "DevOps & Cloud": "8250df",
    "Agile & Sunum": "bf8700",
    "Requirements": "c5def5",
    "Design": "bfd4f2",
    "Development": "0e8a16",
    "Bug": "d73a4a",
    "Git": "f05032",
    "Testing": "fbca04",
    "CI/CD": "5319e7",
    "Docker": "2496ed",
    "Cloud": "0075ca",
    "Monitoring": "006b75",
    "Security": "b60205",
    "Documentation": "0052cc",
    "Agile": "e99695",
    "Presentation": "d4c5f9",
    "Bonus": "ededed",
    "Kubernetes": "326ce5",
}


class ProjectScopeError(RuntimeError):
    """gh token'ında project yetkisi eksik olduğunda fırlatılır."""


def run(cmd: list[str], dry_run: bool, capture: bool = False) -> str:
    printable = " ".join(f'"{c}"' if " " in c else c for c in cmd)
    if dry_run:
        print("  [dry-run]", printable[:160])
        return ""
    result = subprocess.run(cmd, check=False, text=True, capture_output=True)
    if result.returncode != 0:
        err = result.stderr.strip()
        if "project" in cmd and any(
            hint in err.lower() for hint in ("scope", "read:project", "insufficient", "gh auth refresh")
        ):
            raise ProjectScopeError(err)
        raise RuntimeError(f"Komut başarısız: {printable}\n{err}")
    return result.stdout.strip() if capture else ""


def issue_body(task: dict) -> str:
    criteria = "\n".join(f"- [ ] {line}" for line in task["acceptance_criteria"].splitlines() if line.strip())
    return (
        f"**İş akışı:** {task['workflow']} · **Hafta:** {task['week']} ({task['week_dates']}, "
        f"ders hf. {task['course_week']}) · **Öncelik:** {task['priority']} · "
        f"**Tahmini süre:** {task['estimate_hours']} saat · **Branch:** `{task['branch']}`\n\n"
        f"## Task Description\n{task['description']}\n\n"
        f"## Acceptance Criteria\n{criteria}\n\n"
        f"## Evidence\n- {task['evidence']}\n"
        "- [ ] Görev bitince buraya commit / PR / CI run / ekran görüntüsü linkini ekleyin\n"
    )


def create_and_link_project(owner: str, repo: str, title: str, dry_run: bool) -> tuple[int | None, str | None]:
    if dry_run:
        run(["gh", "project", "create", "--owner", owner, "--title", title, "--format", "json"], True)
        run(["gh", "project", "edit", "<N>", "--owner", owner, "--visibility", "PUBLIC"], True)
        run(["gh", "project", "link", "<N>", "--owner", owner, "--repo", repo], True)
        return None, None

    out = run(
        ["gh", "project", "create", "--owner", owner, "--title", title, "--format", "json"],
        False,
        capture=True,
    )
    data = json.loads(out)
    number = int(data["number"])
    url = data.get("url", f"https://github.com/users/{owner}/projects/{number}")
    run(["gh", "project", "edit", str(number), "--owner", owner, "--visibility", "PUBLIC"], False)
    run(["gh", "project", "link", str(number), "--owner", owner, "--repo", repo], False)
    print(f"  Pano oluşturuldu ve depoya bağlandı (Public): {url}")
    return number, url


def existing_project_urls(project_number: int, owner: str) -> set[str]:
    out = run(
        ["gh", "project", "item-list", str(project_number), "--owner", owner, "--limit", "200", "--format", "json"],
        False,
        capture=True,
    )
    items = json.loads(out or "{}").get("items", [])
    urls: set[str] = set()
    for item in items:
        content = item.get("content") or {}
        if content.get("url"):
            urls.add(content["url"])
    return urls


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--repo", required=True, help="sahip/depo-adi")
    parser.add_argument("--project", type=int, help="Mevcut GitHub Projects numarası (isteğe bağlı)")
    parser.add_argument(
        "--create-project",
        action="store_true",
        help="Yeni public GitHub Projects panosu oluşturup depoya bağlar ve kartları ekler",
    )
    parser.add_argument(
        "--project-title",
        default="Etkinlik Kayıt Sistemi - Kanban",
        help="--create-project ile açılacak panonun başlığı",
    )
    parser.add_argument("--owner", help="Proje sahibi (varsayılan: repo sahibi)")
    parser.add_argument("--dry-run", action="store_true", help="Sadece göster, oluşturma")
    args = parser.parse_args()

    if args.project and args.create_project:
        print("--project ve --create-project aynı anda kullanılamaz.", file=sys.stderr)
        return 1

    if not args.dry_run and shutil.which("gh") is None:
        print("GitHub CLI (gh) bulunamadı: https://cli.github.com", file=sys.stderr)
        return 1

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        tasks = list(csv.DictReader(f))
    owner = args.owner or args.repo.split("/")[0]
    weeks = sorted({int(t["week"]) for t in tasks})
    max_week = max(weeks) if weeks else 0

    print(f"1) Etiketler ({len(LABEL_COLORS)})")
    for name, color in LABEL_COLORS.items():
        run(["gh", "label", "create", name, "--repo", args.repo, "--color", color, "--force"], args.dry_run)

    print(f"2) Kilometre taşları (Hafta 1-{max_week})")
    existing_milestones: set[str] = set()
    if not args.dry_run:
        out = run(["gh", "api", f"repos/{args.repo}/milestones?state=all&per_page=100"], False, capture=True)
        existing_milestones = {m["title"] for m in json.loads(out or "[]")}
    for week in weeks:
        title = f"Hafta {week}"
        if title in existing_milestones:
            continue
        dates = next(t["week_dates"] for t in tasks if int(t["week"]) == week)
        run(
            ["gh", "api", f"repos/{args.repo}/milestones"]
            + ["-f", f"title={title}", "-f", f"description={dates}"],
            args.dry_run,
        )

    print(f"3) Issue'lar ({len(tasks)})")
    existing_urls: dict[str, str] = {}
    if not args.dry_run:
        out = run(
            ["gh", "issue", "list", "--repo", args.repo, "--state", "all"]
            + ["--limit", "500", "--json", "title,url"],
            False,
            capture=True,
        )
        existing_urls = {i["title"]: i["url"] for i in json.loads(out or "[]")}

    issue_urls_in_order: list[tuple[str, str]] = []
    for task in tasks:
        title = f"[{task['id']}] {task['title']}"
        if title in existing_urls:
            print(f"  atlandı (zaten var): {title}")
            issue_urls_in_order.append((title, existing_urls[title]))
            continue
        cmd = ["gh", "issue", "create", "--repo", args.repo, "--title", title, "--body", issue_body(task)]
        cmd += ["--milestone", f"Hafta {task['week']}"]
        for label in task["labels"].split(";"):
            cmd += ["--label", label]
        url = run(cmd, args.dry_run, capture=True)
        if not args.dry_run:
            print(f"  oluşturuldu: {title} {url}")
            issue_urls_in_order.append((title, url))

    project_number = args.project
    project_url = f"https://github.com/users/{owner}/projects/{project_number}" if project_number else None

    if args.create_project or project_number:
        print("4) GitHub Projects panosu")
        try:
            if args.create_project:
                project_number, created_url = create_and_link_project(
                    owner, args.repo, args.project_title, args.dry_run
                )
                if created_url:
                    project_url = created_url

            if args.dry_run:
                for task in tasks:
                    run(
                        ["gh", "project", "item-add", str(project_number or "<N>"), "--owner", owner, "--url", f"<{task['id']}>"],
                        True,
                    )
            elif project_number:
                already_in_board = existing_project_urls(project_number, owner)
                added = 0
                for title, url in issue_urls_in_order:
                    if not url or url in already_in_board:
                        continue
                    run(["gh", "project", "item-add", str(project_number), "--owner", owner, "--url", url], False)
                    added += 1
                print(f"  Panoya {added} yeni kart eklendi (toplam kontrol edilen: {len(issue_urls_in_order)}).")
        except ProjectScopeError as exc:
            print(
                "\nUYARI: GitHub CLI oturumunuzda 'project' yetkisi eksik olduğu için pano adımı tamamlanamadı.\n"
                "Etiketler, milestone'lar ve Issue'lar oluşturuldu. Panoyu kurmak için şu iki komutu çalıştırın:\n"
                "  gh auth refresh -s project\n"
                f"  python3 kanban/github_kanban_kur.py --repo {args.repo} --create-project\n"
                f"\nDetay: {exc}",
                file=sys.stderr,
            )
            return 2

    if project_url:
        print(f"\nTamam. Pano adresi: {project_url}")
    else:
        print("\nTamam. Issue'lar ve milestone'lar hazır.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
