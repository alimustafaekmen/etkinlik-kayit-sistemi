# Etkinlik Kayıt Sistemi

YZM6443 Bulut ve DevOps dersi için hazırladığım dönem projesi. Etkinlik oluşturma, katılımcı kaydı ve kontenjan
kontrolü yapan küçük bir web uygulaması olacak.

Proje şu an planlama ve iskelet aşamasında. Kurulum adımları, ekran görüntüleri ve canlı adres ilerleyen haftalarda
eklenecek.

Kanban panosu: https://github.com/users/alimustafaekmen/projects/1

## Planlanan fonksiyonlar

1. Etkinlik oluşturma (ad, açıklama, konum, tarih, kontenjan)
2. Etkinlikleri listeleme ve detay görme
3. Katılımcı kaydı (aynı e-posta ikinci kez kaydolamaz)
4. Kontenjan kontrolü (dolu etkinliğe kayıt alınmaz)
5. E-posta ile kayıt iptali

Gereksinimler [docs/requirements.md](docs/requirements.md), mimari [docs/architecture.md](docs/architecture.md)
dosyasında.

## Teknolojiler

Python 3.12, Flask, SQLite, pytest, Docker, GitHub Actions ve Render kullanmayı planlıyorum.

## Haftalık plan

| Hafta | Tarih | Konu |
|---|---|---|
| 10 | 23-29 Kasım | Kanban, gereksinimler, mimari, proje iskeleti, F1 |
| 11 | 30 Kasım - 6 Aralık | F2-F5 ve web arayüzü |
| 12 | 7-13 Aralık | Testler, CI, Docker |
| 13 | 14-20 Aralık | Render, bulut veritabanı, CD, izleme |
| 14 | 21-27 Aralık | Dokümantasyon, rapor, sunum |
