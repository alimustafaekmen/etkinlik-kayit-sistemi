# Haftalık Kanban ekran görüntüleri

Her pazar panonun tamamı (Todo, In Progress, Issues / Blocked, Done) buraya OnlineBeykoz'un beklediği adla
kaydedilir. Görüntü o haftanın gerçek durumunu gösterir ve sonradan değiştirilmez.

| Hafta | Son gün | Dosya | `make kanban-snapshot WEEK=NN` çıktısı (`submission/dist/`) |
|---|---|---|---|
| 10 | 29 Kasım 2026 | `Kanban_Week_10.png` | `Kanban_Week_10.png`, `Kanban_History_Week_10-10.zip` |
| 11 | 6 Aralık 2026 | `Kanban_Week_11.png` | `Kanban_Week_11.png`, `Kanban_History_Week_10-11.zip` |
| 12 | 13 Aralık 2026 | `Kanban_Week_12.png` | `Kanban_Week_12.png`, `Kanban_History_Week_10-12.zip` |
| 13 | 20 Aralık 2026 | `Kanban_Week_13.png` | `Kanban_Week_13.png`, `Kanban_History_Week_10-13.zip` |
| 14 | 27 Aralık 2026 | `Kanban_Week_14.png` | `Kanban_Week_14.png`, `Kanban_History_Week_10-14.zip` |

PNG yoksa aynı adlı `.jpg` da kabul edilir. Final teslimde `make package` bu klasördeki görüntüleri
`Project_Evidence.zip` içindeki `01_Kanban/` klasörüne ekler.
