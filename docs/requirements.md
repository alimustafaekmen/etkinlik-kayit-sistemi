# Gereksinimler: Etkinlik Kayıt Sistemi

## 1. Amaç ve kapsam

Seminer, atölye, kariyer günü gibi küçük etkinlikleri duyurmak, katılımcı kayıtlarını toplamak ve kontenjan aşımını
önlemek. Dersin odağı Git, test, CI/CD, Docker ve Cloud olduğu için uygulama 5 temel fonksiyonla sınırlı.

Roller: Organizatör (etkinlik oluşturur) ve Katılımcı (kayıt olur / iptal eder). Kimlik doğrulama yok; iki rol aynı
arayüzü kullanır.

## 2. Fonksiyonel gereksinimler

| ID | Gereksinim | Kabul kriterleri |
|---|---|---|
| FR-1 Etkinlik oluşturma | Ad, açıklama (isteğe bağlı), konum, tarih-saat ve kontenjanla etkinlik oluşturulur. | Ad 3–120, konum 2–120 karakter · Tarih gelecekte · Kontenjan 1–10.000 tam sayı · Hatalı girişte alan bazlı mesaj (400) · Başarılıda 201 |
| FR-2 Listeleme ve detay | Etkinlikler tarihe göre listelenir; detayda doluluk, kalan yer ve katılımcılar görünür. | `registered_count`, `remaining_seats`, `is_full` alanları · `?q=` ile ad/konum araması · Olmayan etkinlik 404 · E-postalar maskeli (`al***@ornek.com`) · Durum etiketi: Kayıt açık / Son N yer / Dolu / Sona erdi |
| FR-3 Katılımcı kaydı | Ad soyad ve e-postayla kayıt. | Ad 3–100 karakter · Geçerli e-posta · Aynı e-posta aynı etkinliğe ikinci kez kaydolamaz (büyük/küçük harf duyarsız) → 409 · Başarılıda 201 |
| FR-4 Kontenjan kontrolü | Kayıtlı sayısı kontenjana ulaşınca yeni kayıt reddedilir. | Dolu etkinliğe kayıt → 409 `capacity_full` · Eşzamanlı isteklerde de kontenjan aşılmaz · Geçmiş etkinliğe kayıt → 400 |
| FR-5 Kayıt iptali | Kayıtta kullanılan e-postayla iptal. | Kalan yer 1 artar · Kayıt yoksa 404 · Dolu etkinlikte iptalden sonra yeni kayıt yapılabilir |

## 3. Fonksiyonel olmayan gereksinimler

| ID | Kategori | Gereksinim |
|---|---|---|
| NFR-1 | Test edilebilirlik | En az 3 otomatik birim testi; hedef tüm fonksiyonlar ve %80+ kapsam |
| NFR-2 | Sürekli entegrasyon | Her PR'da lint ve testler otomatik çalışır; kırmızı CI birleştirmeyi engeller |
| NFR-3 | Taşınabilirlik | Docker imajı; tüm ayarlar ortam değişkenlerinden (12-Factor) |
| NFR-4 | Bulut | PaaS (Render) üzerinde HTTPS ile erişim; veriler kalıcı (Neon PostgreSQL) |
| NFR-5 | İzlenebilirlik | `/health`, `/metrics`, JSON loglar, her istekte `X-Request-ID` |
| NFR-6 | Güvenlik | Gizli bilgi kodda yok; root olmayan konteyner; CSRF; güvenlik başlıkları; parametreli SQL; bağımlılık taraması |
| NFR-7 | Kullanılabilirlik | Türkçe arayüz, mobilde okunabilir sayfalar, anlaşılır hata mesajları |

## 4. İş kuralları

- BR-1 `kayıtlı_sayısı ≤ kontenjan` her zaman geçerlidir.
- BR-2 `(etkinlik, e-posta)` çifti benzersizdir.
- BR-3 Geçmiş tarihli etkinlik oluşturulamaz, ona kayıt yapılamaz.
- BR-4 E-postalar küçük harfe çevrilip boşlukları temizlenerek saklanır.

## 5. Kapsam dışı

Kullanıcı hesabı, ödeme, e-posta bildirimi, bekleme listesi, etkinlik düzenleme/silme. Ders yönergesi: "Gelişmiş
arayüz, kullanıcı yönetimi, ödeme sistemi veya karmaşık veritabanı tasarımına gerek yok."

## 6. İzlenebilirlik (gereksinim → kod → test → kart)

| Gereksinim | Kod (`src/etkinlik/`) | Testler (`tests/`) | Kart |
|---|---|---|---|
| FR-1 | `services/events.py` (`validate_event`, `create_event`), `services/validation.py` | `test_events.py`, `test_web.py` | DEV-04 |
| FR-2 | `services/events.py` (`list_events`, `get_event`), `routes/web.py`, `templates/` | `test_events.py`, `test_web.py` | DEV-05, DEV-09 |
| FR-3 | `services/registrations.py` (`register_participant`), `validation.clean_email` | `test_registrations.py` | DEV-06 |
| FR-4 | `register_participant`, `db.transaction()` (SQLite `BEGIN IMMEDIATE`, PostgreSQL `FOR UPDATE`) | `test_registrations.py` (12 thread'li eşzamanlılık testi) | DEV-07 |
| FR-5 | `services/registrations.py` (`cancel_registration`) | `test_registrations.py`, `test_web.py` | DEV-08 |
| NFR-1, NFR-2 | `.github/workflows/ci.yml`, `pyproject.toml` | tüm `tests/` (44 test) | TEST-01, CI-01 |
| NFR-3 | `Dockerfile`, `docker-compose.yml`, `config.py` | CI `docker` job'u | DOCKER-01, CI-02 |
| NFR-4 | `render.yaml`, `cd.yml`, `db.py`, `schema_postgres.sql` | `scripts/smoke_test.sh`, CI PostgreSQL testleri | CLOUD-01, CLOUD-02, CD-01 |
| NFR-5 | `routes/health.py`, `logging_config.py` | `test_health.py` | MON-01, MON-02 |
| NFR-6 | `security.py`, CI `security` job'u, `.github/dependabot.yml` | `test_web.py` (CSRF, başlıklar) | SEC-01, CI-03 |

Kartların tam listesi: [`kanban/tasks.md`](../kanban/tasks.md).

## 7. Demo senaryosu

1. "Docker Atölyesi" kontenjan 2 ile oluşturulur. (FR-1)
2. Listede "Kayıt açık" ve "0 / 2 kayıt · 2 yer kaldı" olarak görünür. (FR-2)
3. Ayşe ve Mehmet kaydolur; etkinlik "Dolu" olur. (FR-3)
4. Zeynep kaydolmaya çalışır, "Kontenjan dolu" mesajını alır. (FR-4)
5. Mehmet kaydını iptal eder, Zeynep kaydolur. (FR-5)
