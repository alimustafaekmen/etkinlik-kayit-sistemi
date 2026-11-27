# Kanban Planı: 5 Haftalık Görev Listesi

Etkinlik Kayıt Sistemi · YZM6443 Modern Yazılım Mühendisliği (Bulut ve DevOps)

Ders 8 hafta üzerinden planlanmış; aşağıdaki plan bunun kalan **5 haftaya** (23 Kasım – 27 Aralık 2026) dengeli şekilde uyarlanmış hâli. "Ders hf." sütunu her haftanın dersin 8 haftalık planındaki karşılığını gösteriyor. Tarihler ders takvimine göre kayabilir.

Toplam **31 kart**, tahmini **76 saat** (haftada yaklaşık 15 saat; 3 saatlik bonus hariç 73 saat). Öncelikler: `P1` zorunlu, `P2` önerilen, `P3` bonus.

## Pano yapısı

| Sütun | Ne zaman? |
|---|---|
| To Do | Başlangıçta tüm kartlar burada |
| In Progress | Üzerinde çalışılan kartlar (aynı anda en fazla 2-3) |
| Issues / Blocked | Takılınan veya hata alınan kartlar (haftalık sunumdaki "Issues/Problems" bölümü) |
| Done | Kabul kriterleri sağlanmış ve Evidence alanı doldurulmuş kartlar |

Etiketler: iş akışı için `Software Development`, `DevOps & Cloud`, `Agile & Sunum`; konu için `Requirements`, `Design`, `Development`, `Bug`, `Git`, `Testing`, `CI/CD`, `Docker`, `Cloud`, `Monitoring`, `Security`, `Documentation`, `Agile`, `Presentation`, `Bonus`, `Kubernetes`.

Kilometre taşları (milestone): her hafta için bir tane, `Hafta 1`'den `Hafta 5`'e kadar.

Her hafta sonu Kanban ekran görüntüsü `haftalik-snapshotlar/hafta-0N_YYYY-AA-GG.png` olarak kaydedilir, kümülatif geçmiş ZIP'i güncellenir ve OnlineBeykoz'a yüklenir.

## Haftalık plan

### Hafta 1 · 23-29 Kasım 2026 · ders hf. 1-2

Odak: Başlangıç (Kanban, Git repo, gereksinimler, mimari, proje iskeleti, F1)

| ID | Görev | İş akışı | Öncelik | Saat | Branch |
|---|---|---|---|---|---|
| PM-01 | Kanban panosunun kurulması | Agile & Sunum | P1 | 1 | `-` |
| GIT-01 | Git deposunun oluşturulması | DevOps & Cloud | P1 | 1 | `main` |
| DEV-01 | Gereksinimlerin belirlenmesi | Software Development | P1 | 2 | `docs/gereksinimler` |
| DEV-02 | Mimari, tasarım ve veri modeli | Software Development | P1 | 2 | `docs/mimari` |
| DEV-03 | Proje iskeleti ve veritabanı katmanı | Software Development | P1 | 3 | `feature/proje-iskeleti` |
| DEV-04 | F1: Etkinlik oluşturma | Software Development | P1 | 3 | `feature/etkinlik-olusturma` |

### Hafta 2 · 30 Kasım - 6 Aralık 2026 · ders hf. 2-3

Odak: Yazılım geliştirme (F2-F5 fonksiyonları, HTML arayüzü, feature branch + Pull Request)

| ID | Görev | İş akışı | Öncelik | Saat | Branch |
|---|---|---|---|---|---|
| DEV-05 | F2: Etkinlik listeleme ve detay | Software Development | P1 | 3 | `feature/etkinlik-listeleme` |
| DEV-06 | F3: Katılımcı kaydı | Software Development | P1 | 3 | `feature/katilimci-kaydi` |
| DEV-07 | F4: Kontenjan kontrolü | Software Development | P1 | 3 | `feature/kontenjan-kontrolu` |
| DEV-08 | F5: Kayıt iptali | Software Development | P1 | 2 | `feature/kayit-iptali` |
| DEV-09 | Web arayüzü (HTML şablonları) | Software Development | P2 | 4 | `feature/web-arayuzu` |
| GIT-02 | Feature branch ve Pull Request akışı | DevOps & Cloud | P1 | 1 | `feature/*` |

### Hafta 3 · 7-13 Aralık 2026 · ders hf. 4-5

Odak: Entegrasyon, otomatik test (pytest), CI pipeline, main koruması ve Docker + Compose

| ID | Görev | İş akışı | Öncelik | Saat | Branch |
|---|---|---|---|---|---|
| DEV-10 | Fonksiyon entegrasyonu ve hata yönetimi | Software Development | P1 | 3 | `feature/entegrasyon` |
| TEST-01 | Otomatik birim testleri (pytest) | DevOps & Cloud | P1 | 4 | `feature/birim-testleri` |
| CI-01 | GitHub Actions CI pipeline | DevOps & Cloud | P1 | 3 | `feature/ci-pipeline` |
| GIT-03 | main dalının korunması | DevOps & Cloud | P2 | 1 | `-` |
| DOCKER-01 | Çok aşamalı Dockerfile ve Docker Compose ortamı | DevOps & Cloud | P1 | 4 | `feature/docker` |
| CI-02 | CI'da Docker build, smoke test ve GHCR push | DevOps & Cloud | P1 | 2 | `feature/ci-docker` |

### Hafta 4 · 14-20 Aralık 2026 · ders hf. 6-7

Odak: Bugfix/iyileştirmeler, Cloud deployment (Render), CD + rollback, monitoring & logging, güvenlik

| ID | Görev | İş akışı | Öncelik | Saat | Branch |
|---|---|---|---|---|---|
| DEV-11 | Hata düzeltme ve iyileştirmeler | Software Development | P2 | 3 | `fix/iyilestirmeler` |
| CLOUD-01 | Render'da yayınlama (PaaS) | DevOps & Cloud | P1 | 3 | `feature/render-deploy` |
| CD-01 | Otomatik dağıtım (CD) | DevOps & Cloud | P1 | 2 | `feature/cd-pipeline` |
| MON-01 | Health check ve metrikler | DevOps & Cloud | P1 | 2 | `feature/monitoring` |
| MON-02 | Yapılandırılmış loglama ve bulut log takibi | DevOps & Cloud | P1 | 2 | `feature/monitoring` |
| SEC-01 | Temel güvenlik kontrolleri | DevOps & Cloud | P2 | 2 | `feature/guvenlik` |

### Hafta 5 · 21-27 Aralık 2026 · ders hf. 8

Odak: Dokümantasyon, fonksiyonel test, v1.0.0 release, final PDF rapor, teslim paketi, sunum ve bonus K8s

| ID | Görev | İş akışı | Öncelik | Saat | Branch |
|---|---|---|---|---|---|
| DOC-01 | README ve mimari dokümanının tamamlanması | DevOps & Cloud | P1 | 2 | `docs/final` |
| TEST-02 | Fonksiyonel testler ve son kontroller | Software Development | P1 | 2 | `-` |
| GIT-04 | Sürüm etiketi ve GitHub Release (v1.0.0) | DevOps & Cloud | P2 | 1 | `main` |
| DOC-02 | Final Project Report (4-6 sayfa PDF) | DevOps & Cloud | P1 | 4 | `-` |
| DOC-03 | Teslim paketi (Links, Evidence, Kanban export, kaynak kod) | DevOps & Cloud | P1 | 2 | `-` |
| PRES-01 | Final sunum ve canlı demo provası | Agile & Sunum | P1 | 3 | `-` |
| BONUS-01 | Bonus: Kubernetes (Minikube) dağıtımı | DevOps & Cloud | P3 | 3 | `feature/k8s` |

## Kart detayları

`github_kanban_kur.py` her kartı aşağıdaki içerikle GitHub Issue olarak açar. Evidence bölümü görev bitince gerçek linklerle doldurulur.

### PM-01 · Kanban panosunun kurulması

*Agile & Sunum · Hafta 1 · P1 · Agile · branch `-`*

Description: GitHub Projects'te To Do, In Progress, Issues/Blocked ve Done sütunlu bir pano oluşturulur ve 5 haftalık görev kartları eklenir.

Acceptance Criteria:

- [ ] Pano en az To Do, In Progress ve Done sütunlarını içeriyor
- [ ] Tüm kartlarda Description, Acceptance Criteria ve Evidence bölümleri var
- [ ] Kanban Board URL'si OnlineBeykoz'a bildirildi

Evidence (beklenen): Kanban Board URL; Hafta 1 Kanban ekran görüntüsü

### GIT-01 · Git deposunun oluşturulması

*DevOps & Cloud · Hafta 1 · P1 · Git · branch `main`*

Description: GitHub'da depo açılır; .gitignore, README taslağı, kanban planı ve şablonlar ilk commit ile eklenir.

Acceptance Criteria:

- [ ] Depo erişilebilir ve ilk commit atılmış
- [ ] .gitignore Python, veritabanı, ders dokümanları ve .env dosyalarını dışarıda bırakıyor
- [ ] README'de proje tanımı ve 5 temel fonksiyon listelenmiş

Evidence (beklenen): Repository URL; ilk commit linki

### DEV-01 · Gereksinimlerin belirlenmesi

*Software Development · Hafta 1 · P1 · Requirements · branch `docs/gereksinimler`*

Description: 5 temel fonksiyon, fonksiyonel / fonksiyonel olmayan gereksinimler ve iş kuralları (kontenjan, mükerrer kayıt) yazılır.

Acceptance Criteria:

- [ ] docs/requirements.md içinde FR ve NFR listesi var
- [ ] Her fonksiyon için kabul kriteri tanımlı
- [ ] Kapsam dışı maddeler (kullanıcı yönetimi, ödeme vb.) belirtilmiş

Evidence (beklenen): docs/requirements.md commit linki

### DEV-02 · Mimari, tasarım ve veri modeli

*Software Development · Hafta 1 · P1 · Design · branch `docs/mimari`*

Description: Katmanlı mimari (routes → services → SQLite), REST API uç noktaları ve events / registrations veri modeli tasarlanır.

Acceptance Criteria:

- [ ] docs/architecture.md içinde mimari diyagramı var
- [ ] ER diyagramı ve tablo alanları tanımlı
- [ ] API uç noktaları ve dönüş kodları listelenmiş

Evidence (beklenen): docs/architecture.md commit linki

### DEV-03 · Proje iskeleti ve veritabanı katmanı

*Software Development · Hafta 1 · P1 · Development · branch `feature/proje-iskeleti`*

Description: Flask uygulama fabrikası, ortam değişkenli yapılandırma, SQLite bağlantısı ve şema oluşturulur.

Acceptance Criteria:

- [ ] `flask --app wsgi run` ile uygulama açılıyor
- [ ] İlk açılışta tablolar otomatik oluşturuluyor
- [ ] Ayarlar (SECRET_KEY, DATABASE_PATH vb.) ortam değişkenlerinden okunuyor

Evidence (beklenen): PR linki; çalışan uygulamanın ekran görüntüsü

### DEV-04 · F1: Etkinlik oluşturma

*Software Development · Hafta 1 · P1 · Development · branch `feature/etkinlik-olusturma`*

Description: Ad, açıklama, konum, tarih ve kontenjan bilgisiyle etkinlik oluşturma (API + doğrulama) geliştirilir.

Acceptance Criteria:

- [ ] POST /api/events geçerli veride 201 döndürüyor
- [ ] Eksik/hatalı alanlarda 400 ve alan bazlı hata mesajı dönüyor
- [ ] Geçmiş tarihli veya kontenjanı 1'den küçük etkinlik oluşturulamıyor

Evidence (beklenen): PR linki; curl veya Postman çıktısı

### DEV-05 · F2: Etkinlik listeleme ve detay

*Software Development · Hafta 2 · P1 · Development · branch `feature/etkinlik-listeleme`*

Description: Etkinlikler tarihe göre listelenir; detayda doluluk (kayıtlı/kontenjan) ve kalan yer gösterilir; ad/konum araması eklenir.

Acceptance Criteria:

- [ ] GET /api/events tarihe göre sıralı liste döndürüyor
- [ ] Her etkinlikte registered_count ve remaining_seats alanları var
- [ ] ?q= parametresiyle ad veya konuma göre arama çalışıyor

Evidence (beklenen): PR linki; API çıktısı

### DEV-06 · F3: Katılımcı kaydı

*Software Development · Hafta 2 · P1 · Development · branch `feature/katilimci-kaydi`*

Description: Ad soyad ve e-posta ile etkinliğe kayıt yapılır; aynı e-postanın aynı etkinliğe ikinci kez kaydı engellenir.

Acceptance Criteria:

- [ ] Geçerli kayıt 201 döndürüyor
- [ ] Aynı e-posta (büyük/küçük harf fark etmeksizin) 409 döndürüyor
- [ ] Geçersiz e-posta veya kısa ad 400 döndürüyor

Evidence (beklenen): PR linki; API çıktısı

### DEV-07 · F4: Kontenjan kontrolü

*Software Development · Hafta 2 · P1 · Development · branch `feature/kontenjan-kontrolu`*

Description: Kayıt sayısı kontenjana ulaşınca yeni kayıt reddedilir; eşzamanlı isteklerde kontenjanın aşılmaması için BEGIN IMMEDIATE transaction kullanılır.

Acceptance Criteria:

- [ ] Dolu etkinliğe kayıt 409 capacity_full döndürüyor
- [ ] Kayıtlı sayısı hiçbir durumda kontenjanı aşmıyor
- [ ] Arayüzde dolu etkinlik 'Dolu' etiketiyle görünüyor

Evidence (beklenen): PR linki; 409 yanıtının ekran görüntüsü

### DEV-08 · F5: Kayıt iptali

*Software Development · Hafta 2 · P1 · Development · branch `feature/kayit-iptali`*

Description: Katılımcı, kayıtta kullandığı e-posta ile kaydını iptal eder; boşalan yer yeniden kullanılabilir hale gelir.

Acceptance Criteria:

- [ ] İptal sonrası kalan yer sayısı 1 artıyor
- [ ] Olmayan kayıt için 404 dönüyor
- [ ] Dolu etkinlikte iptal sonrası yeni kayıt yapılabiliyor

Evidence (beklenen): PR linki; API çıktısı

### DEV-09 · Web arayüzü (HTML şablonları)

*Software Development · Hafta 2 · P2 · Development · branch `feature/web-arayuzu`*

Description: Etkinlik listesi, oluşturma formu ve detay/kayıt/iptal sayfaları basit bir HTML arayüzle sunulur.

Acceptance Criteria:

- [ ] 5 fonksiyonun tamamı tarayıcıdan kullanılabiliyor
- [ ] Başarı ve hata mesajları kullanıcıya gösteriliyor
- [ ] Sayfalar mobil ekranda okunabilir

Evidence (beklenen): PR linki; arayüz ekran görüntüleri

### GIT-02 · Feature branch ve Pull Request akışı

*DevOps & Cloud · Hafta 2 · P1 · Git · branch `feature/*`*

Description: Her fonksiyon ayrı bir feature branch'te geliştirilir ve Pull Request ile main'e birleştirilir; PR'lar ilgili kartlara bağlanır.

Acceptance Criteria:

- [ ] En az 2 (hedef 5+) feature branch ve merge edilmiş PR var
- [ ] PR açıklamalarında 'Closes #<kart>' ile kart bağlantısı var
- [ ] Commit mesajları anlamlı (feat:, fix:, docs:, test:, ci:)

Evidence (beklenen): PR listesi linki; Insights > Network grafiği ekran görüntüsü

### DEV-10 · Fonksiyon entegrasyonu ve hata yönetimi

*Software Development · Hafta 3 · P1 · Development · branch `feature/entegrasyon`*

Description: Tüm fonksiyonlar tek uygulamada birleştirilir; ortak hata yönetimi (JSON hata biçimi, 404/500 sayfaları) eklenir.

Acceptance Criteria:

- [ ] Tüm API hataları {error, message} biçiminde dönüyor
- [ ] Tam senaryo (oluştur, kayıt, dolu, iptal, tekrar kayıt) çalışıyor
- [ ] Bilinmeyen sayfalarda 404 sayfası gösteriliyor

Evidence (beklenen): PR linki; senaryo adımlarının ekran görüntüleri

### TEST-01 · Otomatik birim testleri (pytest)

*DevOps & Cloud · Hafta 3 · P1 · Testing · branch `feature/birim-testleri`*

Description: pytest ile servis katmanı ve API için birim testleri yazılır; her test kendi geçici veritabanını kullanır.

Acceptance Criteria:

- [ ] En az 3 test (hedef 15+) yazıldı ve geçiyor
- [ ] Kontenjan, mükerrer kayıt ve iptal senaryoları test ediliyor
- [ ] Kod kapsamı (coverage) %80'in üzerinde

Evidence (beklenen): pytest çıktısı ekran görüntüsü; coverage raporu

### CI-01 · GitHub Actions CI pipeline

*DevOps & Cloud · Hafta 3 · P1 · CI/CD · branch `feature/ci-pipeline`*

Description: Her push ve Pull Request'te lint (ruff) ve testleri (pytest + coverage) çalıştıran CI iş akışı kurulur.

Acceptance Criteria:

- [ ] .github/workflows/ci.yml depoda mevcut
- [ ] Push ve PR'da otomatik tetikleniyor ve yeşil bitiyor
- [ ] Bir test bozulduğunda pipeline kırmızıya dönüyor

Evidence (beklenen): Başarılı Actions run linki; bilerek bozulan testle kırmızı run ekran görüntüsü

### GIT-03 · main dalının korunması

*DevOps & Cloud · Hafta 3 · P2 · Git · branch `-`*

Description: main dalına doğrudan push engellenir; birleştirme yalnızca CI'ı geçen Pull Request ile yapılabilir.

Acceptance Criteria:

- [ ] Branch protection kuralı (veya ruleset) aktif
- [ ] 'Require status checks to pass' seçili ve CI testi zorunlu
- [ ] CI'ı kırmızı olan PR birleştirilemiyor

Evidence (beklenen): Ayar sayfası ekran görüntüsü

### DOCKER-01 · Çok aşamalı Dockerfile ve Docker Compose ortamı

*DevOps & Cloud · Hafta 3 · P1 · Docker · branch `feature/docker`*

Description: Çok aşamalı Dockerfile (builder, dev, runtime; /opt/venv, root olmayan kullanıcı, Gunicorn, HEALTHCHECK) ve kalıcı volume'lü + geliştirme profilli docker-compose.yml hazırlanır.

Acceptance Criteria:

- [ ] `docker build` ve `docker run -p 8000:8000` başarıyla çalışıyor; `docker ps` çıktısında konteyner (healthy) görünüyor
- [ ] `docker compose up --build` ile uygulama kalıcı volume ile açılıyor
- [ ] `docker compose run --rm dev pytest` testleri konteynerde çalıştırıyor

Evidence (beklenen): docker build / run / ps ve docker compose çıktıları

### CI-02 · CI'da Docker build, smoke test ve GHCR push

*DevOps & Cloud · Hafta 3 · P1 · CI/CD, Docker · branch `feature/ci-docker`*

Description: CI testlerden sonra Docker image oluşturur, konteyneri çalıştırıp smoke test yapar ve main'de image'ı GitHub Container Registry'ye gönderir.

Acceptance Criteria:

- [ ] docker job'u yeşil bitiyor
- [ ] Konteyner içinde /health smoke testi geçiyor
- [ ] Image GitHub > Packages altında görünüyor

Evidence (beklenen): Actions run linki; Packages sayfası ekran görüntüsü

### DEV-11 · Hata düzeltme ve iyileştirmeler

*Software Development · Hafta 4 · P2 · Development, Bug · branch `fix/iyilestirmeler`*

Description: Önceki haftalarda testlerde ve denemelerde bulunan hatalar giderilir; doğrulama mesajları ve arayüz iyileştirilir.

Acceptance Criteria:

- [ ] Açık hata (bug) kartları kapatıldı
- [ ] Her düzeltme için bir regresyon testi eklendi
- [ ] CI yeşil

Evidence (beklenen): fix/* PR linkleri

### CLOUD-01 · Render'da yayınlama (PaaS)

*DevOps & Cloud · Hafta 4 · P1 · Cloud · branch `feature/render-deploy`*

Description: render.yaml Blueprint ile Docker tabanlı web servisi Render'da (ücretsiz plan, Frankfurt) oluşturulur.

Acceptance Criteria:

- [ ] Uygulama https://<servis>.onrender.com adresinde açılıyor
- [ ] Render health check (/health) başarılı
- [ ] SECRET_KEY Render'da üretildi, kodda yer almıyor

Evidence (beklenen): Cloud Application URL; Render dashboard ekran görüntüsü

### CD-01 · Otomatik dağıtım (CD)

*DevOps & Cloud · Hafta 4 · P1 · CI/CD, Cloud · branch `feature/cd-pipeline`*

Description: CI main'de başarılı olunca GitHub Actions, test edilen commit'i (ref=<sha>) Render'a dağıtır, yeni sürümü bekler, canlı ortamda smoke test yapar; başarısızlıkta önceki sürüme geri döner.

Acceptance Criteria:

- [ ] cd.yml CI'dan sonra otomatik çalışıyor ve yalnızca CI'dan geçen commit'i dağıtıyor
- [ ] /health yanıtındaki commit, son commit ile aynı; canlı smoke testi geçiyor
- [ ] Elle geri dönüş (Run workflow + commit SHA) denendi

Evidence (beklenen): CD run linki; GitHub > Environments > production geçmişi

### MON-01 · Health check ve metrikler

*DevOps & Cloud · Hafta 4 · P1 · Monitoring · branch `feature/monitoring`*

Description: /health (veritabanı kontrolü, sürüm, commit, uptime) ve /metrics (istek sayıları, ortalama yanıt süresi, iş metrikleri) uç noktaları sunulur.

Acceptance Criteria:

- [ ] /health sağlıklıyken 200, veritabanı hatasında 503 döndürüyor
- [ ] /metrics istek ve iş metriklerini gösteriyor
- [ ] Render > Metrics ekranı (CPU, bellek, istek) incelendi

Evidence (beklenen): /health JSON çıktısı; Render Metrics ekran görüntüsü

### MON-02 · Yapılandırılmış loglama ve bulut log takibi

*DevOps & Cloud · Hafta 4 · P1 · Monitoring · branch `feature/monitoring`*

Description: Her istek ve iş olayı (kayıt, kontenjan reddi, iptal) JSON log olarak yazılır ve Render Logs ekranında izlenir.

Acceptance Criteria:

- [ ] Loglarda method, path, status, duration_ms, request_id alanları var
- [ ] Kontenjan reddi WARNING seviyesinde loglanıyor
- [ ] Render Logs ekranında arama ile ilgili olay bulunabiliyor

Evidence (beklenen): Render Logs ekran görüntüsü

### SEC-01 · Temel güvenlik kontrolleri

*DevOps & Cloud · Hafta 4 · P2 · Security · branch `feature/guvenlik`*

Description: Gizli anahtarlar ortam değişkeninde tutulur; konteyner root olmayan kullanıcıyla çalışır; CSRF koruması, güvenlik başlıkları ve bağımlılık taraması (pip-audit) eklenir.

Acceptance Criteria:

- [ ] Depoda gizli bilgi yok (.env Git'e eklenmiyor)
- [ ] Yanıtlarda güvenlik başlıkları (CSP, X-Frame-Options vb.) var
- [ ] pip-audit CI'da çalışıyor

Evidence (beklenen): `curl -I` çıktısı; pip-audit job çıktısı

### DOC-01 · README ve mimari dokümanının tamamlanması

*DevOps & Cloud · Hafta 5 · P1 · Documentation · branch `docs/final`*

Description: README'ye kurulum, çalıştırma, API örnekleri, CI/CD ve canlı linkler; architecture.md'ye son mimari eklenir.

Acceptance Criteria:

- [ ] README'deki adımlarla temiz bir makinede kurulum yapılabiliyor
- [ ] README'de CI rozeti (badge) ve canlı URL var
- [ ] docs/architecture.md güncel

Evidence (beklenen): README ve docs commit linkleri

### TEST-02 · Fonksiyonel testler ve son kontroller

*Software Development · Hafta 5 · P1 · Testing · branch `-`*

Description: Canlı ortamda 5 fonksiyon baştan sona elle test edilir, smoke test çalıştırılır ve bulunan sorunlar giderilir.

Acceptance Criteria:

- [ ] Fonksiyonel test tablosu (senaryo / beklenen / gerçek) dolduruldu
- [ ] Canlı ortam smoke testi geçiyor
- [ ] Açık kritik hata kalmadı

Evidence (beklenen): Final rapordaki test tablosu; smoke test çıktısı

### GIT-04 · Sürüm etiketi ve GitHub Release (v1.0.0)

*DevOps & Cloud · Hafta 5 · P2 · Git · branch `main`*

Description: Final sürüm v1.0.0 etiketiyle işaretlenir ve GitHub Release oluşturulur.

Acceptance Criteria:

- [ ] `git tag v1.0.0` oluşturulup push edildi
- [ ] GitHub Release sayfasında sürüm notları var

Evidence (beklenen): Release linki

### DOC-02 · Final Project Report (4-6 sayfa PDF)

*DevOps & Cloud · Hafta 5 · P1 · Documentation · branch `-`*

Description: Ödevde istenen 7 bölümlük teknik rapor hazırlanır ve PDF'e dönüştürülür.

Acceptance Criteria:

- [ ] 7 bölümün tamamı yazıldı
- [ ] Uygulama, CI/CD, Docker, Render ve Kanban ekran görüntüleri eklendi
- [ ] PDF 4-6 sayfa arasında

Evidence (beklenen): Final_Project_Report.pdf

### DOC-03 · Teslim paketi (Links, Evidence, Kanban export, kaynak kod)

*DevOps & Cloud · Hafta 5 · P1 · Documentation · branch `-`*

Description: Project_Links.txt, Project_Evidence.zip (haftalık Kanban görüntüleri ve kanıtlar), Kanban CSV export ve kaynak kod zip'i hazırlanır.

Acceptance Criteria:

- [ ] Project_Links.txt içindeki tüm linkler çalışıyor
- [ ] Evidence ZIP'inde 5 haftalık Kanban görüntüsü var
- [ ] Kanban export'ta tüm kartların Description / Acceptance Criteria / Evidence alanları dolu

Evidence (beklenen): OnlineBeykoz teslim ekranı

### PRES-01 · Final sunum ve canlı demo provası

*Agile & Sunum · Hafta 5 · P1 · Presentation · branch `-`*

Description: 5-7 dakikalık sunum hazırlanır; uygulama, Git, CI/CD, Docker ve Cloud süreçleri canlı gösterilir.

Acceptance Criteria:

- [ ] Sunum 7 dakikayı aşmıyor
- [ ] Demo senaryosu (kayıt, dolu, iptal, yeniden kayıt) prova edildi
- [ ] Render uyku modundan dolayı uygulama sunumdan birkaç dakika önce açıldı

Evidence (beklenen): Sunum dosyası

### BONUS-01 · Bonus: Kubernetes (Minikube) dağıtımı

*DevOps & Cloud · Hafta 5 · P3 · Bonus, Kubernetes · branch `feature/k8s`*

Description: (İsteğe bağlı) Docker image Minikube'a Deployment + Service olarak dağıtılır; probe'lar /health kullanır.

Acceptance Criteria:

- [ ] `kubectl get pods` çıktısında pod Running ve READY 1/1
- [ ] Readiness / liveness probe'ları /health uç noktasını kullanıyor
- [ ] Servis tarayıcıdan açılıyor

Evidence (beklenen): kubectl çıktıları ekran görüntüsü
