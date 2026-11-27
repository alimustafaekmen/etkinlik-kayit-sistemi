# Kanban

Proje **GitHub Projects** panosunda takip ediliyor. Kartlar GitHub Issue olduğu için commit ve Pull Request'ler
karta bağlanıyor; PR açıklamasına `Closes #12` yazınca PR birleşince kart kendiliğinden Done'a geçiyor.

- **Pano:** https://github.com/users/alimustafaekmen/projects/1 (public, 5 hafta boyunca aynı URL)
- **Kartlar:** [`tasks.md`](tasks.md) (okunabilir) ve [`tasks.csv`](tasks.csv) (asıl kaynak; pano betiği bunu okur).
  32 kart, 5 hafta: Hafta 10 = 23–29 Kasım … Hafta 14 = 21–27 Aralık 2026.
- **Haftalık görüntüler:** [`screenshots/`](screenshots/)

## Pano

| Sütun (Status) | Anlamı |
|---|---|
| Todo | Planlandı, başlanmadı |
| In Progress | Üzerinde çalışılıyor (aynı anda en fazla 2–3 kart) |
| Issues / Blocked | Takıldım veya hata var; nedeni karta yorum olarak yazılır |
| Done | Kabul kriterleri sağlandı, Evidence gerçek linklerle dolu |

Alanlar: `Hafta` (Hafta 10–14), `Alan` (Software Development · DevOps & Cloud · Agile & Sunum), `Öncelik` (P1 · P2),
`Tahmin (saat)`. Her hafta bir milestone (`Hafta N`, bitişi pazar).

**Kart biçimi:** başlık `[ID] Görev adı`; gövdede `Task Description` (1–2 cümle), `Acceptance Criteria`
(2–3 maddelik kontrol listesi) ve `Evidence` (commit, PR, Actions run, canlı URL, ekran görüntüsü).

## Kurulum (bir kez)

```bash
gh auth login && gh auth refresh -s project              # 'project' yetkisi pano için gerekli
python3 scripts/setup_kanban.py --dry-run --create-project   # önce planı gör (GitHub'a yazmaz)
python3 scripts/setup_kanban.py --create-project             # etiketler, milestone'lar, 32 issue, pano
```

Betik tekrar çalıştırılabilir; var olanları yeniden oluşturmaz ve elle taşınan kartların Status'unu değiştirmez.
Sonra GitHub'da: Board görünümü (Column by: Status) ve pano `⋯ > Workflows` içinde "Item closed" ile
"Pull request merged" → Done açık olmalı.

## Kart yaşam döngüsü

```
Todo ──(branch aç)──> In Progress ──(PR birleşti, kriterler tamam)──> Done
                          └──(hata / engel)──> Issues / Blocked ──(çözüldü)──┘
```

1. Kartı In Progress'e al, karttaki branch'i aç (`git switch -c feature/...`).
2. PR aç, açıklamaya `Closes #<issue>` yaz. Takılırsan kartı Issues / Blocked'a al.
3. PR birleşince kart Done olur; Acceptance Criteria kutularını işaretle, Evidence'a gerçek linkleri yaz.
4. Plan dışı iş (ör. hata) için "Görev kartı (Kanban)" şablonuyla yeni issue aç (`Bug` etiketi, `Hafta N`).

## Haftalık rutin (her pazar)

1. Kart durumlarını ve Evidence linklerini güncelle.
2. Board görünümünün ekran görüntüsünü al (dört sütun görünmeli) ve
   `kanban/screenshots/Kanban_Week_NN.png` olarak kaydet.
3. `make kanban-snapshot WEEK=NN` → `submission/dist/` altında `Kanban_Week_NN.png` ve
   `Kanban_History_Week_10-NN.zip` oluşur.
4. Bu iki dosyayı ve pano URL'sini OnlineBeykoz'a yükle; görüntüyü commit'le (`docs: Hafta N Kanban görüntüsü`).

## Final export

- `tasks.csv` ve `tasks.md` içindeki `status` ve `evidence` değerlerini gerçek linklerle güncelle;
  `make package` `tasks.csv`'yi ve 5 haftalık görüntüyü `Project_Evidence.zip` içindeki `01_Kanban/` klasörüne koyar.
- Panodan da CSV al: Table görünümü > görünüm menüsü > *Export view data*; dosyayı
  `submission/Project_Evidence/01_Kanban/` içine koy (issue gövdesi bu export'ta olmadığı için `tasks.csv` de teslim edilir).
