# Etkinlik Kayıt Sistemi

> **Durum: Hafta 10 — planlama ve iskelet.** Bu README projenin ilk haftasındaki hâlidir; kurulum adımları,
> ekran görüntüleri ve canlı adres uygulama geliştikçe eklenecek.

Etkinlik oluşturma, katılımcı kaydı ve kontenjan kontrolü yapan küçük bir web uygulaması. YZM6443 Modern Yazılım
Mühendisliği (Bulut ve DevOps) dersinin dönem projesi.

**Amaç:** Uygulamayı bilerek küçük tutup Kanban, Git (feature branch + Pull Request), otomatik test, CI/CD, Docker,
bulut dağıtımı ve izleme adımlarını 5 haftada tek projede uçtan uca uygulamak.

| Bağlantı | Adres |
|---|---|
| Kanban panosu | https://github.com/users/alimustafaekmen/projects/1 |
| Görev kartları | [`kanban/tasks.md`](kanban/tasks.md) (32 kart, 5 hafta) |

## Planlanan temel fonksiyonlar

| # | Fonksiyon | Hafta |
|---|---|---|
| F1 | Etkinlik oluşturma (ad, açıklama, konum, tarih, kontenjan) | 10 |
| F2 | Etkinlikleri listeleme, arama ve detay (kayıtlı sayısı, kalan yer) | 11 |
| F3 | Katılımcı kaydı (aynı e-posta aynı etkinliğe ikinci kez kaydolamaz) | 11 |
| F4 | Kontenjan kontrolü (dolu etkinliğe kayıt reddedilir) | 11 |
| F5 | E-posta ile kayıt iptali (boşalan yer yeniden açılır) | 11 |

## Gereksinimler (özet)

- Etkinlik gelecekte bir tarihte ve 1–10.000 kontenjanla oluşturulur; hatalı alanlar Türkçe ve alan alan bildirilir.
- Etkinlikler tarihe göre listelenir; kontenjan dolunca veya tarih geçince kayıt alınmaz.
- Aynı anda gelen kayıt istekleri kontenjanı aşamaz.
- Hem web arayüzü (HTML formlar) hem JSON API olacak.
- Fonksiyonel olmayan: en az 3 otomatik test, CI/CD, Docker, bulutta (PaaS) yayın, `/health` ve JSON loglar, gizli
  bilgilerin ortam değişkeninde tutulması.

Ayrıntılar: [`docs/requirements.md`](docs/requirements.md) · Mimari: [`docs/architecture.md`](docs/architecture.md)

## Planlanan teknolojiler ve pipeline

Python 3.12 · Flask · SQLite (yerel) / PostgreSQL (canlı) · pytest · Ruff · Docker · GitHub Actions · Render

```
feature branch → Pull Request → CI (lint + test + Docker build) → main → CD → Render (canlı)
```

## 5 haftalık plan

| Hafta | Tarih | Odak |
|---|---|---|
| 10 | 23–29 Kasım 2026 | Kanban, depo, gereksinimler, mimari, proje iskeleti, F1 |
| 11 | 30 Kasım – 6 Aralık 2026 | F2–F5, web arayüzü, PR akışı |
| 12 | 7–13 Aralık 2026 | Entegrasyon, birim testleri, CI, Docker |
| 13 | 14–20 Aralık 2026 | Render + bulut veritabanı, CD, izleme, güvenlik |
| 14 | 21–27 Aralık 2026 | Dokümantasyon, final testler, sürüm, rapor ve sunum |
