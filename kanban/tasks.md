# Kanban Planı: 5 Haftalık Görev Listesi

Etkinlik Kayıt Sistemi · YZM6443 Modern Yazılım Mühendisliği (Bulut ve DevOps)

Ders 8 hafta üzerinden planlanmış; proje **5 haftada** (23 Kasım – 27 Aralık 2026) tamamlanıyor. Toplam **32 kart**, tahmini **75 saat**. Öncelik: `P1` zorunlu, `P2` önerilen.

Kartların asıl kaynağı [`tasks.csv`](tasks.csv); `scripts/setup_kanban.py` panoyu bu dosyadan kuruyor. Bu sayfa aynı içeriğin okunabilir hâli; bir kart değişince ikisi birlikte güncelleniyor. Sütunlar, alanlar ve haftalık rutin için bkz. [`README.md`](README.md).

## Haftalık plan

| Hafta | Tarih | Kart | Saat | Odak |
|---|---|---|---|---|
| Hafta 10 | 23–29 Kasım 2026 | 6 | 12 | Kanban panosu, Git deposu, gereksinimler, mimari, proje iskeleti, F1 |
| Hafta 11 | 30 Kasım – 6 Aralık 2026 | 6 | 16 | F2–F5 fonksiyonları, web arayüzü, feature branch + Pull Request akışı |
| Hafta 12 | 7–13 Aralık 2026 | 7 | 17 | Entegrasyon, otomatik testler, CI, main koruması, Dependabot, Docker |
| Hafta 13 | 14–20 Aralık 2026 | 7 | 16 | Hata düzeltme, Render'a yayınlama, Neon PostgreSQL, CD, izleme ve loglama, güvenlik |
| Hafta 14 | 21–27 Aralık 2026 | 6 | 14 | Son dokümantasyon, fonksiyonel testler, v1.0.0, final rapor, teslim paketi, sunum |
| **Toplam** | | **32** | **75** | |

### Hafta 10 · 23–29 Kasım 2026

| ID | Görev | Alan | Öncelik | Saat | Durum | Branch |
|---|---|---|---|---|---|---|
| PM-01 | Kanban panosunun kurulması | Agile & Sunum | P1 | 1 | Todo | `-` |
| GIT-01 | Git deposunun oluşturulması | DevOps & Cloud | P1 | 1 | Done | `main` |
| DEV-01 | Gereksinimlerin belirlenmesi | Software Development | P1 | 2 | Todo | `docs/gereksinimler` |
| DEV-02 | Mimari, tasarım ve veri modeli | Software Development | P1 | 2 | Todo | `docs/mimari` |
| DEV-03 | Proje iskeleti ve veritabanı katmanı | Software Development | P1 | 3 | Todo | `feature/proje-iskeleti` |
| DEV-04 | F1: Etkinlik oluşturma | Software Development | P1 | 3 | Todo | `feature/etkinlik-olusturma` |

### Hafta 11 · 30 Kasım – 6 Aralık 2026

| ID | Görev | Alan | Öncelik | Saat | Durum | Branch |
|---|---|---|---|---|---|---|
| DEV-05 | F2: Etkinlik listeleme ve detay | Software Development | P1 | 3 | Todo | `feature/etkinlik-listeleme` |
| DEV-06 | F3: Katılımcı kaydı | Software Development | P1 | 3 | Todo | `feature/katilimci-kaydi` |
| DEV-07 | F4: Kontenjan kontrolü | Software Development | P1 | 3 | Todo | `feature/kontenjan-kontrolu` |
| DEV-08 | F5: Kayıt iptali | Software Development | P1 | 2 | Todo | `feature/kayit-iptali` |
| DEV-09 | Web arayüzü (HTML şablonları) | Software Development | P2 | 4 | Todo | `feature/web-arayuzu` |
| GIT-02 | Feature branch ve Pull Request akışı | DevOps & Cloud | P1 | 1 | Todo | `docs/git-akisi` |

### Hafta 12 · 7–13 Aralık 2026

| ID | Görev | Alan | Öncelik | Saat | Durum | Branch |
|---|---|---|---|---|---|---|
| DEV-10 | Fonksiyon entegrasyonu ve hata yönetimi | Software Development | P1 | 3 | Todo | `feature/entegrasyon` |
| TEST-01 | Otomatik birim testleri (pytest) | DevOps & Cloud | P1 | 4 | Todo | `feature/birim-testleri` |
| CI-01 | GitHub Actions CI pipeline | DevOps & Cloud | P1 | 3 | Todo | `feature/ci-pipeline` |
| GIT-03 | main dalının korunması | DevOps & Cloud | P2 | 1 | Todo | `-` |
| CI-03 | Dependabot ile otomatik bağımlılık güncellemeleri | DevOps & Cloud | P2 | 1 | Todo | `feature/dependabot` |
| DOCKER-01 | Çok aşamalı Dockerfile ve Docker Compose | DevOps & Cloud | P1 | 3 | Todo | `feature/docker` |
| CI-02 | CI'da Docker build, smoke test ve GHCR push | DevOps & Cloud | P1 | 2 | Todo | `feature/ci-docker` |

### Hafta 13 · 14–20 Aralık 2026

| ID | Görev | Alan | Öncelik | Saat | Durum | Branch |
|---|---|---|---|---|---|---|
| DEV-11 | Hata düzeltme ve iyileştirmeler | Software Development | P2 | 3 | Todo | `fix/iyilestirmeler` |
| CLOUD-01 | Render'da yayınlama (PaaS) | DevOps & Cloud | P1 | 3 | Todo | `feature/render-deploy` |
| CLOUD-02 | Bulut veritabanı (Neon PostgreSQL) | DevOps & Cloud | P2 | 2 | Todo | `feature/bulut-veritabani` |
| CD-01 | Otomatik dağıtım (CD) | DevOps & Cloud | P1 | 2 | Todo | `feature/cd-pipeline` |
| MON-01 | Health check ve metrikler | DevOps & Cloud | P1 | 2 | Todo | `feature/monitoring` |
| MON-02 | Yapılandırılmış loglama ve bulut log takibi | DevOps & Cloud | P1 | 2 | Todo | `feature/monitoring` |
| SEC-01 | Temel güvenlik kontrolleri | DevOps & Cloud | P2 | 2 | Todo | `feature/guvenlik` |

### Hafta 14 · 21–27 Aralık 2026

| ID | Görev | Alan | Öncelik | Saat | Durum | Branch |
|---|---|---|---|---|---|---|
| DOC-01 | README ve mimari dokümanının tamamlanması | DevOps & Cloud | P1 | 2 | Todo | `docs/final` |
| TEST-02 | Fonksiyonel testler ve son kontroller | Software Development | P1 | 2 | Todo | `-` |
| GIT-04 | Sürüm etiketi ve GitHub Release (v1.0.0) | DevOps & Cloud | P2 | 1 | Todo | `main` |
| DOC-02 | Final Project Report (4–6 sayfa PDF) | DevOps & Cloud | P1 | 4 | Todo | `-` |
| DOC-03 | Teslim paketi (Links, Evidence, Kanban export, kaynak kod) | DevOps & Cloud | P1 | 2 | Todo | `docs/final` |
| PRES-01 | Final sunum ve canlı demo provası | Agile & Sunum | P1 | 3 | Todo | `-` |

## Ders gereksinimlerinin kartlara dağılımı

| | Yönergedeki madde | Kart(lar) |
|---|---|---|
| A | Gereksinimlerin belirlenmesi | DEV-01 |
| A | Mimari, tasarım ve veri modeli | DEV-02, DEV-03 |
| A | 3–5 temel fonksiyon | DEV-04 (F1), DEV-05 (F2), DEV-06 (F3), DEV-07 (F4), DEV-08 (F5) |
| A | Fonksiyonların entegrasyonu | DEV-09, DEV-10 |
| A | Hata düzeltme ve iyileştirmeler | DEV-11 |
| A | Fonksiyonel testler ve son kontroller | TEST-02 |
| B | Git & Version Control (Branch, Merge, PR) | GIT-01, GIT-02, GIT-03, GIT-04 |
| B | Automated Testing | TEST-01 |
| B | CI/CD Pipeline | CI-01, CI-02, CI-03, CD-01 |
| B | Docker & Containerization | DOCKER-01, CI-02 |
| B | Cloud Deployment | CLOUD-01, CLOUD-02, CD-01 |
| B | Monitoring & Logging | MON-01, MON-02 |
| B | Documentation | DOC-01, DOC-02, DOC-03 |
| + | Agile / Kanban ve sunum | PM-01, PRES-01 |
| + | Güvenlik | SEC-01, CI-03 |

## Kart detayları

Her kart GitHub Issue olarak `[ID] Görev adı` başlığıyla açılıyor. Evidence maddeleri görev bitince gerçek linklerle değiştiriliyor.

### PM-01 · Kanban panosunun kurulması

*Hafta 10 · Agile & Sunum · P1 · 1 saat · Todo · Branch: `-` · Etiketler: `Agile & Sunum`, `Agile`*

**Task Description:** GitHub Projects'te Todo, In Progress, Issues / Blocked ve Done sütunlu public bir pano kurulur; 32 görev kartı scripts/setup_kanban.py ile GitHub Issue olarak panoya eklenir.

**Acceptance Criteria:**

- [ ] Panoda Todo, In Progress, Issues / Blocked ve Done sütunları var
- [ ] Her kartta Task Description, Acceptance Criteria ve Evidence ile Hafta, Alan, Öncelik alanları dolu
- [ ] Pano URL'si OnlineBeykoz'a bildirildi ve kanban/screenshots/Kanban_Week_10.png kaydedildi

**Evidence:**

- Kanban Board URL (https://github.com/users/alimustafaekmen/projects/1)
- Kanban_Week_10.png ve Kanban_History_Week_10-10.zip (OnlineBeykoz Hafta 10 teslimi)

### GIT-01 · Git deposunun oluşturulması

*Hafta 10 · DevOps & Cloud · P1 · 1 saat · Done · Branch: `main` · Etiketler: `DevOps & Cloud`, `Git`*

**Task Description:** GitHub'da public depo açılır; README, .gitignore, Kanban planı ve Issue / PR şablonları ilk commit ile main'e eklenir.

**Acceptance Criteria:**

- [x] Depo public ve ilk commit main'de
- [x] .gitignore Python önbelleklerini, yerel veritabanını ve .env dosyalarını dışarıda bırakıyor
- [x] README'de proje tanımı ve 5 temel fonksiyon listelenmiş

**Evidence:**

- Repository: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi
- İlk commit: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/commit/edf84f9

### DEV-01 · Gereksinimlerin belirlenmesi

*Hafta 10 · Software Development · P1 · 2 saat · Todo · Branch: `docs/gereksinimler` · Etiketler: `Software Development`, `Requirements`*

**Task Description:** 5 temel fonksiyon (F1–F5), fonksiyonel ve fonksiyonel olmayan gereksinimler ile iş kuralları (kontenjan, mükerrer kayıt) docs/requirements.md'de yazılır.

**Acceptance Criteria:**

- [ ] docs/requirements.md içinde FR ve NFR listesi var
- [ ] Her fonksiyon için kabul kriteri tanımlı
- [ ] Kapsam dışı maddeler (kullanıcı yönetimi, ödeme vb.) belirtilmiş

**Evidence:**

- docs/gereksinimler PR linki (docs/requirements.md)

### DEV-02 · Mimari, tasarım ve veri modeli

*Hafta 10 · Software Development · P1 · 2 saat · Todo · Branch: `docs/mimari` · Etiketler: `Software Development`, `Design`*

**Task Description:** Katmanlı mimari (routes → services → db.py), REST API uç noktaları ve events / registrations veri modeli docs/architecture.md'de tasarlanır.

**Acceptance Criteria:**

- [ ] Mimari diyagramı ve src/etkinlik klasör yapısı açıklanmış
- [ ] ER diyagramı ve tablo alanları src/etkinlik/schema.sql ile uyumlu
- [ ] API uç noktaları ve dönüş kodları listelenmiş

**Evidence:**

- docs/mimari PR linki (docs/architecture.md)

### DEV-03 · Proje iskeleti ve veritabanı katmanı

*Hafta 10 · Software Development · P1 · 3 saat · Todo · Branch: `feature/proje-iskeleti` · Etiketler: `Software Development`, `Development`*

**Task Description:** src/etkinlik paketinde Flask uygulama fabrikası (create_app), ortam değişkenli config.py, SQLite katmanı (db.py, schema.sql) ve /health uç noktası oluşturulur; geliştirme ortamı uv ile .venv (Python 3.12).

**Acceptance Criteria:**

- [ ] `.venv/bin/flask run` ile uygulama http://127.0.0.1:8000 adresinde açılıyor ve /health 200 dönüyor
- [ ] İlk açılışta tablolar otomatik oluşturuluyor
- [ ] SECRET_KEY, DATABASE_PATH gibi ayarlar ortam değişkenlerinden okunuyor (.env.example, .flaskenv)

**Evidence:**

- feature/proje-iskeleti PR linki
- Çalışan uygulamanın ve /health yanıtının ekran görüntüsü

### DEV-04 · F1: Etkinlik oluşturma

*Hafta 10 · Software Development · P1 · 3 saat · Todo · Branch: `feature/etkinlik-olusturma` · Etiketler: `Software Development`, `Development`*

**Task Description:** Ad, açıklama, konum, tarih ve kontenjanla etkinlik oluşturma; doğrulama (services/validation.py, services/events.py) ve POST /api/events uç noktası yazılır.

**Acceptance Criteria:**

- [ ] POST /api/events geçerli veride 201 döndürüyor
- [ ] Eksik veya hatalı alanlarda 400 ve alan bazlı Türkçe hata mesajı dönüyor
- [ ] Geçmiş tarihli veya kontenjanı 1'den küçük etkinlik oluşturulamıyor

**Evidence:**

- feature/etkinlik-olusturma PR linki
- curl ile 201 ve 400 yanıtlarının çıktısı

### DEV-05 · F2: Etkinlik listeleme ve detay

*Hafta 11 · Software Development · P1 · 3 saat · Todo · Branch: `feature/etkinlik-listeleme` · Etiketler: `Software Development`, `Development`*

**Task Description:** Etkinlikler tarihe göre listelenir (GET /api/events, GET /api/events/{id}); her etkinlikte doluluk ve kalan yer gösterilir, ad veya konuma göre arama yapılabilir.

**Acceptance Criteria:**

- [ ] GET /api/events tarihe göre sıralı liste döndürüyor
- [ ] Her etkinlikte registered_count ve remaining_seats alanları var
- [ ] ?q= parametresiyle ad veya konuma göre arama çalışıyor

**Evidence:**

- feature/etkinlik-listeleme PR linki
- GET /api/events?q=... çıktısı

### DEV-06 · F3: Katılımcı kaydı

*Hafta 11 · Software Development · P1 · 3 saat · Todo · Branch: `feature/katilimci-kaydi` · Etiketler: `Software Development`, `Development`*

**Task Description:** Ad soyad ve e-posta ile etkinliğe kayıt yapılır (services/registrations.py); aynı e-postanın aynı etkinliğe ikinci kez kaydı engellenir.

**Acceptance Criteria:**

- [ ] Geçerli kayıt 201 döndürüyor
- [ ] Aynı e-posta (büyük/küçük harf fark etmeksizin) 409 duplicate_registration döndürüyor
- [ ] Geçersiz e-posta, kısa ad veya geçmiş etkinliğe kayıt 400 döndürüyor

**Evidence:**

- feature/katilimci-kaydi PR linki
- POST /api/events/{id}/registrations çıktısı (201 ve 409)

### DEV-07 · F4: Kontenjan kontrolü

*Hafta 11 · Software Development · P1 · 3 saat · Todo · Branch: `feature/kontenjan-kontrolu` · Etiketler: `Software Development`, `Development`*

**Task Description:** Kayıt sayısı kontenjana ulaşınca yeni kayıt reddedilir; aynı anda gelen isteklerde kontenjanın aşılmaması için sayım ve kayıt db.py'deki transaction içinde (SQLite: BEGIN IMMEDIATE) yapılır.

**Acceptance Criteria:**

- [ ] Dolu etkinliğe kayıt 409 capacity_full döndürüyor
- [ ] Aynı anda gelen isteklerde de kayıtlı sayısı kontenjanı aşmıyor

**Evidence:**

- feature/kontenjan-kontrolu PR linki
- 409 capacity_full yanıtının ekran görüntüsü

### DEV-08 · F5: Kayıt iptali

*Hafta 11 · Software Development · P1 · 2 saat · Todo · Branch: `feature/kayit-iptali` · Etiketler: `Software Development`, `Development`*

**Task Description:** Katılımcı, kayıtta kullandığı e-posta ile kaydını iptal eder (POST /api/events/{id}/registrations/cancel); boşalan yer yeniden kullanılabilir.

**Acceptance Criteria:**

- [ ] İptal sonrası kalan yer sayısı 1 artıyor
- [ ] Olmayan kayıt için 404 dönüyor
- [ ] Dolu etkinlikte iptal sonrası yeni kayıt yapılabiliyor

**Evidence:**

- feature/kayit-iptali PR linki
- İptal öncesi ve sonrası remaining_seats çıktısı

### DEV-09 · Web arayüzü (HTML şablonları)

*Hafta 11 · Software Development · P2 · 4 saat · Todo · Branch: `feature/web-arayuzu` · Etiketler: `Software Development`, `Development`*

**Task Description:** Etkinlik listesi, oluşturma formu ve detay / kayıt / iptal sayfaları routes/web.py ve templates/ ile sunulur; seed.py 6 örnek etkinlik yükler.

**Acceptance Criteria:**

- [ ] 5 fonksiyonun tamamı tarayıcıdan kullanılabiliyor; formlar CSRF korumalı
- [ ] Kartlarda doluluk çubuğu ve Kayıt açık / Son N yer / Dolu / Sona erdi etiketi görünüyor
- [ ] Sayfalar mobil ekranda (390 px) yatay kaydırma olmadan okunuyor

**Evidence:**

- feature/web-arayuzu PR linki
- docs/images/ ekran görüntüleri (etkinlik-listesi.png, etkinlik-detay-kayit.png, etkinlik-formu-dogrulama.png, etkinlik-mobil.png)

### GIT-02 · Feature branch ve Pull Request akışı

*Hafta 11 · DevOps & Cloud · P1 · 1 saat · Todo · Branch: `docs/git-akisi` · Etiketler: `DevOps & Cloud`, `Git`*

**Task Description:** Her fonksiyon ayrı bir feature branch'te geliştirilir ve Pull Request ile main'e birleştirilir; akış docs/git-workflow.md'de belgelenir.

**Acceptance Criteria:**

- [ ] En az 2 (hedef 5+) feature branch PR ile main'e birleştirildi
- [ ] PR açıklamalarında 'Closes #N' ile kart bağlantısı var; PR birleşince kart Done'a geçiyor
- [ ] Commit mesajları anlamlı (feat:, fix:, docs:, test:, ci:)

**Evidence:**

- docs/git-akisi PR linki (docs/git-workflow.md)
- Birleştirilmiş PR listesi: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/pulls?q=is%3Apr+is%3Amerged
- Insights > Network grafiği ekran görüntüsü (submission/Project_Evidence/03_Git/)

### DEV-10 · Fonksiyon entegrasyonu ve hata yönetimi

*Hafta 12 · Software Development · P1 · 3 saat · Todo · Branch: `feature/entegrasyon` · Etiketler: `Software Development`, `Development`*

**Task Description:** Tüm fonksiyonlar tek uygulamada birleştirilir; ortak hata yönetimi (errors.py ve uygulama fabrikasındaki hata yakalayıcı: JSON hata biçimi, Türkçe 404 / 500 sayfaları) eklenir.

**Acceptance Criteria:**

- [ ] Tüm API hataları {error, message} biçiminde dönüyor
- [ ] Tam senaryo (oluştur, kayıt, dolu, iptal, tekrar kayıt) uçtan uca çalışıyor
- [ ] Bilinmeyen sayfalarda Türkçe 404 sayfası gösteriliyor

**Evidence:**

- feature/entegrasyon PR linki
- Senaryo adımlarının ekran görüntüleri (submission/Project_Evidence/02_Software/)

### TEST-01 · Otomatik birim testleri (pytest)

*Hafta 12 · DevOps & Cloud · P1 · 4 saat · Todo · Branch: `feature/birim-testleri` · Etiketler: `DevOps & Cloud`, `Testing`*

**Task Description:** tests/ altında pytest ile 5 test dosyası yazılır (test_events, test_registrations, test_web, test_health, test_db); her test kendi geçici SQLite veritabanını kullanır.

**Acceptance Criteria:**

- [ ] En az 3 test (projede 44) `.venv/bin/pytest -v --cov` ile geçiyor
- [ ] Kontenjan (eşzamanlı istekler dahil), mükerrer kayıt ve iptal senaryoları test ediliyor
- [ ] Kod kapsamı (coverage) %80'in üzerinde

**Evidence:**

- feature/birim-testleri PR linki
- pytest ve coverage çıktısının ekran görüntüsü (submission/Project_Evidence/04_Testing/)

### CI-01 · GitHub Actions CI pipeline

*Hafta 12 · DevOps & Cloud · P1 · 3 saat · Todo · Branch: `feature/ci-pipeline` · Etiketler: `DevOps & Cloud`, `CI/CD`*

**Task Description:** Her push ve Pull Request'te lint (ruff check + format) ve testleri (pytest, kapsam en az %80) çalıştıran .github/workflows/ci.yml iş akışı kurulur.

**Acceptance Criteria:**

- [ ] ci.yml push ve PR'da otomatik tetikleniyor ve yeşil bitiyor
- [ ] Bir test bozulduğunda pipeline kırmızıya dönüyor
- [ ] Run sayfasındaki Summary bölümünde kapsam tablosu görünüyor

**Evidence:**

- Başarılı Actions run linki
- Bilerek bozulan testle kırmızı run ekran görüntüsü (submission/Project_Evidence/05_CI/)

### GIT-03 · main dalının korunması

*Hafta 12 · DevOps & Cloud · P2 · 1 saat · Todo · Branch: `-` · Etiketler: `DevOps & Cloud`, `Git`*

**Task Description:** main dalına doğrudan push engellenir; birleştirme yalnızca CI'dan geçen Pull Request ile yapılabilir.

**Acceptance Criteria:**

- [ ] Branch protection kuralı (veya ruleset) main için aktif
- [ ] 'Require status checks to pass' seçili ve CI test job'u zorunlu
- [ ] CI'ı kırmızı olan PR birleştirilemiyor

**Evidence:**

- Settings > Branches (Rules) ekran görüntüsü (submission/Project_Evidence/05_CI/)

### CI-03 · Dependabot ile otomatik bağımlılık güncellemeleri

*Hafta 12 · DevOps & Cloud · P2 · 1 saat · Todo · Branch: `feature/dependabot` · Etiketler: `DevOps & Cloud`, `CI/CD`, `Security`*

**Task Description:** .github/dependabot.yml ile pip paketleri, GitHub Actions ve Docker temel imajı için haftalık güncelleme PR'ları açılır; bu PR'lar da CI'dan geçmeden birleştirilmez.

**Acceptance Criteria:**

- [ ] .github/dependabot.yml main'e birleştirildi
- [ ] Dependabot bir PR açtı ve CI o PR'da çalıştı

**Evidence:**

- feature/dependabot PR linki
- Dependabot PR'ları: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/pulls?q=is%3Apr+author%3Aapp%2Fdependabot

### DOCKER-01 · Çok aşamalı Dockerfile ve Docker Compose

*Hafta 12 · DevOps & Cloud · P1 · 3 saat · Todo · Branch: `feature/docker` · Etiketler: `DevOps & Cloud`, `Docker`*

**Task Description:** Çok aşamalı Dockerfile (base, builder, runtime; root olmayan kullanıcı, Gunicorn + deploy/gunicorn.conf.py, HEALTHCHECK), tek web servisli docker-compose.yml ve sık komutlar için Makefile hazırlanır.

**Acceptance Criteria:**

- [ ] `make docker-build` ve `docker run -p 8000:8000` çalışıyor; `docker ps` çıktısında konteyner (healthy)
- [ ] `make up` ile uygulama kalıcı volume ile açılıyor ve `make smoke` geçiyor
- [ ] Konteyner root olmayan kullanıcıyla (appuser) çalışıyor

**Evidence:**

- feature/docker PR linki
- docker build / run / ps ve docker compose çıktıları (submission/Project_Evidence/06_Docker/)

### CI-02 · CI'da Docker build, smoke test ve GHCR push

*Hafta 12 · DevOps & Cloud · P1 · 2 saat · Todo · Branch: `feature/ci-docker` · Etiketler: `DevOps & Cloud`, `CI/CD`, `Docker`*

**Task Description:** CI testlerden sonra Docker image oluşturur, konteyneri scripts/smoke_test.sh ile test eder ve main'de image'ı GitHub Container Registry'ye (GHCR) gönderir.

**Acceptance Criteria:**

- [ ] ci.yml içindeki docker job'u yeşil bitiyor
- [ ] Konteynere karşı smoke test ve /health commit kontrolü geçiyor
- [ ] Image GitHub > Packages altında görünüyor

**Evidence:**

- docker job'unun Actions run linki
- GHCR paket sayfası: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/pkgs/container/etkinlik-kayit-sistemi

### DEV-11 · Hata düzeltme ve iyileştirmeler

*Hafta 13 · Software Development · P2 · 3 saat · Todo · Branch: `fix/iyilestirmeler` · Etiketler: `Software Development`, `Development`, `Bug`*

**Task Description:** Testlerde ve denemelerde bulunan hatalar fix/* branch'lerinde giderilir; doğrulama mesajları ve arayüz iyileştirilir.

**Acceptance Criteria:**

- [ ] Açık Bug etiketli kartlar kapatıldı
- [ ] Her düzeltme için bir regresyon testi eklendi
- [ ] CI yeşil

**Evidence:**

- fix/* PR linkleri ve ilgili regresyon testleri

### CLOUD-01 · Render'da yayınlama (PaaS)

*Hafta 13 · DevOps & Cloud · P1 · 3 saat · Todo · Branch: `feature/render-deploy` · Etiketler: `DevOps & Cloud`, `Cloud`*

**Task Description:** render.yaml Blueprint ile Docker tabanlı web servisi Render'da (ücretsiz plan, Frankfurt) oluşturulur; adımlar docs/deployment.md'de anlatılır.

**Acceptance Criteria:**

- [ ] Uygulama https://etkinlik-kayit-sistemi.onrender.com adresinde açılıyor
- [ ] Render health check (/health) başarılı
- [ ] SECRET_KEY Render'da üretildi, kodda yer almıyor

**Evidence:**

- Cloud Application URL: https://etkinlik-kayit-sistemi.onrender.com
- Render dashboard ekran görüntüsü (submission/Project_Evidence/07_Cloud/)

### CLOUD-02 · Bulut veritabanı (Neon PostgreSQL)

*Hafta 13 · DevOps & Cloud · P2 · 2 saat · Todo · Branch: `feature/bulut-veritabani` · Etiketler: `DevOps & Cloud`, `Cloud`*

**Task Description:** Render'ın ücretsiz planında SQLite verisi her deploy'da silindiği için Neon'da ücretsiz PostgreSQL açılır; DATABASE_URL verilince db.py PostgreSQL'e bağlanır (kontenjan için SELECT ... FOR UPDATE).

**Acceptance Criteria:**

- [ ] Neon projesi oluşturuldu ve DATABASE_URL Render'da tanımlandı (depoda yok)
- [ ] /health yanıtında "database": "postgresql" görünüyor
- [ ] Veriler yeniden deploy sonrasında korunuyor
- [ ] CI'daki PostgreSQL test adımı yeşil

**Evidence:**

- feature/bulut-veritabani PR linki
- Canlı /health çıktısı ve Neon panel ekran görüntüsü (submission/Project_Evidence/07_Cloud/)

### CD-01 · Otomatik dağıtım (CD)

*Hafta 13 · DevOps & Cloud · P1 · 2 saat · Todo · Branch: `feature/cd-pipeline` · Etiketler: `DevOps & Cloud`, `CI/CD`, `Cloud`*

**Task Description:** CI main'de başarılı olunca .github/workflows/cd.yml test edilen commit'i scripts/deploy_render.sh ile Render'a dağıtır ve scripts/smoke_test.sh ile canlı ortamı test eder.

**Acceptance Criteria:**

- [ ] cd.yml yalnızca main'de CI yeşil bitince (veya elle Run workflow ile) çalışıyor
- [ ] /health yanıtındaki commit dağıtılan commit ile aynı; canlı smoke testi geçiyor
- [ ] RENDER_DEPLOY_HOOK_URL secret, APP_URL variable olarak tanımlı; kodda yok

**Evidence:**

- CD run linki ve Summary ekran görüntüsü (submission/Project_Evidence/08_CD/)
- Deploy geçmişi: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/deployments/production

### MON-01 · Health check ve metrikler

*Hafta 13 · DevOps & Cloud · P1 · 2 saat · Todo · Branch: `feature/monitoring` · Etiketler: `DevOps & Cloud`, `Monitoring`*

**Task Description:** /health (veritabanı kontrolü, motor, sürüm, commit, uptime) ve /metrics (istek sayısı, ortalama yanıt süresi, etkinlik ve kayıt sayıları) routes/health.py'de sunulur.

**Acceptance Criteria:**

- [ ] /health sağlıklıyken 200, veritabanı hatasında 503 döndürüyor
- [ ] /metrics istek ve iş metriklerini gösteriyor
- [ ] Render > Metrics ekranı (CPU, bellek, istek) incelendi

**Evidence:**

- Canlı /health ve /metrics JSON çıktısı
- Render Metrics ekran görüntüsü (submission/Project_Evidence/09_Monitoring/)

### MON-02 · Yapılandırılmış loglama ve bulut log takibi

*Hafta 13 · DevOps & Cloud · P1 · 2 saat · Todo · Branch: `feature/monitoring` · Etiketler: `DevOps & Cloud`, `Monitoring`*

**Task Description:** Her istek ve iş olayı (kayıt, kontenjan reddi, iptal) logging_config.py ile request_id'li JSON log olarak yazılır ve Render Logs ekranında izlenir.

**Acceptance Criteria:**

- [ ] Loglarda method, path, status, duration_ms, request_id alanları var
- [ ] Kontenjan reddi WARNING seviyesinde loglanıyor
- [ ] Render Logs ekranında arama ile ilgili olay (ör. capacity_full) bulunabiliyor

**Evidence:**

- Render Logs ekran görüntüsü (submission/Project_Evidence/09_Monitoring/)

### SEC-01 · Temel güvenlik kontrolleri

*Hafta 13 · DevOps & Cloud · P2 · 2 saat · Todo · Branch: `feature/guvenlik` · Etiketler: `DevOps & Cloud`, `Security`*

**Task Description:** Gizli anahtarlar ortam değişkeninde tutulur; CSRF koruması ve güvenlik başlıkları (security.py) ile CI'da bağımlılık taraması (pip-audit) eklenir.

**Acceptance Criteria:**

- [ ] Depoda gizli bilgi yok (.env Git'e eklenmiyor); konteyner root olmayan kullanıcıyla çalışıyor
- [ ] Yanıtlarda güvenlik başlıkları (CSP, X-Frame-Options vb.) var
- [ ] pip-audit CI'daki security job'unda çalışıyor

**Evidence:**

- `curl -I` ile güvenlik başlıkları çıktısı
- security (pip-audit) job'unun Actions run linki

### DOC-01 · README ve mimari dokümanının tamamlanması

*Hafta 14 · DevOps & Cloud · P1 · 2 saat · Todo · Branch: `docs/final` · Etiketler: `DevOps & Cloud`, `Documentation`*

**Task Description:** README'ye kurulum, çalıştırma, API örnekleri, CI/CD ve canlı linkler; docs/architecture.md ve docs/deployment.md'ye son durum eklenir.

**Acceptance Criteria:**

- [ ] README'deki adımlarla (make setup, make run) temiz bir makinede kurulum yapılabiliyor
- [ ] README'de CI rozeti (badge), canlı URL ve Kanban linki var
- [ ] docs/architecture.md ve docs/deployment.md güncel

**Evidence:**

- docs/final PR linki

### TEST-02 · Fonksiyonel testler ve son kontroller

*Hafta 14 · Software Development · P1 · 2 saat · Todo · Branch: `-` · Etiketler: `Software Development`, `Testing`*

**Task Description:** Canlı ortamda 5 fonksiyon baştan sona elle test edilir, scripts/smoke_test.sh çalıştırılır ve bulunan sorunlar giderilir.

**Acceptance Criteria:**

- [ ] Fonksiyonel test tablosu (senaryo / beklenen / gerçek) dolduruldu
- [ ] Canlı ortam smoke testi geçiyor (`APP_URL=https://etkinlik-kayit-sistemi.onrender.com make smoke`)
- [ ] Açık kritik hata kalmadı

**Evidence:**

- Final rapordaki fonksiyonel test tablosu
- Canlı smoke test çıktısı

### GIT-04 · Sürüm etiketi ve GitHub Release (v1.0.0)

*Hafta 14 · DevOps & Cloud · P2 · 1 saat · Todo · Branch: `main` · Etiketler: `DevOps & Cloud`, `Git`*

**Task Description:** Final sürüm v1.0.0 etiketiyle işaretlenir ve sürüm notlarıyla GitHub Release oluşturulur.

**Acceptance Criteria:**

- [ ] `git tag v1.0.0` oluşturulup push edildi
- [ ] GitHub Release sayfasında sürüm notları var

**Evidence:**

- Release linki: https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/releases/tag/v1.0.0

### DOC-02 · Final Project Report (4–6 sayfa PDF)

*Hafta 14 · DevOps & Cloud · P1 · 4 saat · Todo · Branch: `-` · Etiketler: `DevOps & Cloud`, `Documentation`*

**Task Description:** submission/Final_Project_Report.md taslağı ödevdeki 7 bölümle tamamlanır ve Final_Project_Report.pdf olarak dışa aktarılır.

**Acceptance Criteria:**

- [ ] 7 bölümün tamamı yazıldı
- [ ] Uygulama, CI/CD, Docker, Render ve Kanban ekran görüntüleri eklendi
- [ ] PDF 4–6 sayfa arasında

**Evidence:**

- submission/Final_Project_Report.pdf (OnlineBeykoz final teslimi)

### DOC-03 · Teslim paketi (Links, Evidence, Kanban export, kaynak kod)

*Hafta 14 · DevOps & Cloud · P1 · 2 saat · Todo · Branch: `docs/final` · Etiketler: `DevOps & Cloud`, `Documentation`*

**Task Description:** submission/Project_Links.txt doldurulur; `make package` ile Project_Evidence.zip ve kaynak kod zip'i submission/dist/ altında hazırlanır.

**Acceptance Criteria:**

- [ ] Project_Links.txt içindeki tüm linkler çalışıyor
- [ ] Project_Evidence.zip içinde 5 haftalık Kanban görüntüsü, tasks.csv ve kanıt klasörleri var
- [ ] Kanban CSV export'unda tüm kartların Description / Acceptance Criteria / Evidence alanları dolu

**Evidence:**

- submission/dist/ içeriği ve OnlineBeykoz teslim ekranı görüntüsü

### PRES-01 · Final sunum ve canlı demo provası

*Hafta 14 · Agile & Sunum · P1 · 3 saat · Todo · Branch: `-` · Etiketler: `Agile & Sunum`, `Presentation`*

**Task Description:** 5–7 dakikalık final sunumu hazırlanır; uygulama, Git, CI/CD, Docker, Cloud ve Kanban süreci canlı gösterilir (docs/weekly-progress.md notlarından).

**Acceptance Criteria:**

- [ ] Sunum 7 dakikayı aşmıyor
- [ ] Demo senaryosu (oluştur, kayıt, dolu, iptal, yeniden kayıt) prova edildi
- [ ] Render uyku modu nedeniyle uygulama sunumdan birkaç dakika önce açıldı

**Evidence:**

- Sunum dosyası ve demo senaryosu
