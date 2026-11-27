# Kanban

Projeyi GitHub Projects panosunda takip ediyorum: https://github.com/users/alimustafaekmen/projects/1

Kartlar GitHub Issue olarak açıldı (32 kart, Hafta 10-14). Kartların listesi [tasks.csv](tasks.csv) dosyasında da var.

## Sütunlar

- Todo: planlandı, başlanmadı
- In Progress: üzerinde çalışıyorum
- Issues / Blocked: takıldığım işler, nedeni karta yorum olarak yazılır
- Done: tamamlandı

## Kart formatı

Başlık `[ID] Görev adı` şeklinde (ör. `[DEV-04] Etkinlik oluşturma`). Her kartta üç bölüm var:

- Açıklama (Description)
- Kabul Kriterleri (Acceptance Criteria)
- Kanıt (Evidence): PR, commit, CI çalışması veya ekran görüntüsü linki

PR açıklamasına `Closes #<issue>` yazınca PR merge olduğunda kart Done'a geçiyor.

## Haftalık rutin

Her pazar:

1. Kartların durumunu ve kanıt linklerini güncelliyorum.
2. Panonun ekran görüntüsünü `kanban/screenshots/Kanban_Week_NN.png` olarak kaydediyorum.
3. `bash scripts/kanban_snapshot.sh NN` ile teslim dosyalarını hazırlayıp OnlineBeykoz'a yüklüyorum.
