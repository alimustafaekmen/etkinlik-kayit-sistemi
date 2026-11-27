# Etkinlik Kayıt Sistemi

[![CI](https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/actions/workflows/ci.yml/badge.svg)](https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/actions/workflows/ci.yml)
[![CD](https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/actions/workflows/cd.yml/badge.svg)](https://github.com/alimustafaekmen/etkinlik-kayit-sistemi/actions/workflows/cd.yml)

Etkinlik oluşturma, katılımcı kaydı ve kontenjan kontrolü yapan küçük bir web uygulaması. YZM6443 Modern Yazılım
Mühendisliği (Bulut ve DevOps) dersinin dönem projesi olarak geliştirdim. Uygulamayı bilerek küçük tuttum; asıl amaç
Git, otomatik test, CI/CD, Docker, Render'a dağıtım ve izleme adımlarını tek bir projede uygulamaktı.

| | |
|---|---|
| Canlı uygulama | https://etkinlik-kayit-sistemi.onrender.com *(Render adresi değişirse güncellenecek)* |
| Kanban panosu | https://github.com/users/alimustafaekmen/projects/1 |
| Teknolojiler | Python 3.12 · Flask 3 · SQLite · Gunicorn · pytest · Ruff · Docker · GitHub Actions · Render |

![Etkinlik listesi](docs/ekran-goruntuleri/etkinlik-listesi.png)

## Temel fonksiyonlar

| # | Fonksiyon | Web | API |
|---|---|---|---|
| F1 | Etkinlik oluşturma (ad, açıklama, konum, tarih, kontenjan) | `/events/new` | `POST /api/events` |
| F2 | Etkinlik listeleme ve detay (doluluk, kalan yer, arama) | `/`, `/events/<id>` | `GET /api/events?q=`, `GET /api/events/<id>` |
| F3 | Katılımcı kaydı (ad soyad, e-posta; mükerrer kayıt engeli) | detay sayfası | `POST /api/events/<id>/registrations` |
| F4 | Kontenjan kontrolü (dolu etkinliğe kayıt 409 ile reddedilir) | "Dolu" etiketi | `409 capacity_full` |
| F5 | Kayıt iptali (e-posta ile; yer yeniden açılır) | detay sayfası | `POST /api/events/<id>/registrations/cancel` |

İzleme için iki uç nokta var: `GET /health` (sağlık kontrolü) ve `GET /metrics` (istek ve iş metrikleri).

## Fonksiyonel gereksinimler (özet)

- FR-1 Kullanıcı ad, konum, gelecekte bir tarih ve 1-10.000 arası kontenjan ile etkinlik oluşturabilir.
- FR-2 Etkinlikler tarihe göre sıralı listelenir; her etkinlikte kayıtlı sayısı ve kalan yer görünür; ad/konuma göre aranabilir.
- FR-3 Katılımcı ad soyad ve geçerli bir e-posta ile kaydolur; aynı e-posta aynı etkinliğe ikinci kez kaydolamaz.
- FR-4 Kayıtlı sayısı kontenjana ulaşınca yeni kayıt reddedilir; tarihi geçmiş etkinliğe kayıt yapılamaz.
- FR-5 Katılımcı e-postasıyla kaydını iptal edebilir; boşalan yer başka katılımcıya açılır.

Ayrıntılar [`docs/requirements.md`](docs/requirements.md) dosyasında, mimari ve veri modeli
[`docs/architecture.md`](docs/architecture.md) dosyasında.

## Kurulum ve çalıştırma

### 1) Yerelde (Python)

```bash
git clone https://github.com/alimustafaekmen/etkinlik-kayit-sistemi.git
cd etkinlik-kayit-sistemi
python3 -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
SEED_DEMO_DATA=true flask --app wsgi run --debug --port 8000
```
Uygulama http://127.0.0.1:8000 adresinde açılır.

### 2) Docker geliştirme ortamı (bilgisayara Python kurmadan)

Python ve paketler imajın içindeki sanal ortama (`/opt/venv`) kurulur. Proje klasörü konteynere bağlandığı için
koddaki değişiklikler hemen yansır ve sunucu kendini yeniden başlatır.

```bash
docker compose build dev                                  # venv'i oluştur, paketleri indir (bir kez)
docker compose up dev                                     # http://localhost:8000 (Ctrl+C ile durdur)

docker compose run --rm dev pytest -v --cov=app           # testler konteynerde
docker compose run --rm dev ruff check .                  # lint konteynerde
docker compose run --rm dev pip list                      # venv'deki paketler
docker compose run --rm dev bash                          # konteynerde kabuk (shell)
```

Yeni paket eklemek için önce `requirements.txt` (veya `requirements-dev.txt`) güncellenir, sonra
`docker compose build dev` çalıştırılır.

### 3) Docker üretim imajı (Render'da çalışanla aynı)

```bash
docker build -t etkinlik-kayit-sistemi .
docker run --rm -p 8000:8000 -e SEED_DEMO_DATA=true -e SESSION_COOKIE_SECURE=false etkinlik-kayit-sistemi
# veya kalıcı volume ile:
docker compose up --build
```
Dockerfile'da `HEALTHCHECK` tanımlı olduğu için `docker ps` çıktısında konteyner `(healthy)` görünür.

| Dockerfile aşaması | İçerik | Kim kullanır |
|---|---|---|
| `builder` | `/opt/venv` + `requirements.txt` paketleri | diğer aşamalar |
| `dev` | builder + `requirements-dev.txt` (pytest, ruff, pip-audit), Flask debug sunucusu | `docker compose … dev` |
| `runtime` (varsayılan) | yalnızca `/opt/venv` + uygulama kodu, root olmayan kullanıcı, Gunicorn | CI, Render, `docker build .` |

### 4) Testler ve kod kalitesi (yerel Python ile)

```bash
pytest -v --cov=app          # testler + kapsam raporu
ruff check . && ruff format --check .
```
Makefile kısayolları: `make test`, `make lint`, `make run`, `make docker-build`, `make docker-run`,
`make compose-up`, `make smoke`.

### Ortam değişkenleri

| Değişken | Varsayılan | Açıklama |
|---|---|---|
| `SECRET_KEY` | `dev-secret-degistirin` | Oturum/CSRF anahtarı. Üretimde mutlaka değiştirilmeli (Render otomatik üretiyor) |
| `DATABASE_PATH` | `data/events.db` | SQLite dosyası |
| `APP_ENV` | `development` | `production` olduğunda güvenli çerez ve proxy ayarları açılır (Docker imajında varsayılan `production`) |
| `SESSION_COOKIE_SECURE` | üretimde `true` | Yerelde Docker ile HTTP üzerinden denerken formların çalışması için `false` verilmeli |
| `SEED_DEMO_DATA` | `false` | `true` ise boş veritabanına 3 örnek etkinlik eklenir |
| `LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`… |
| `APP_TIMEZONE` | `Europe/Istanbul` | Geçmiş tarih kontrolü için saat dilimi |
| `PORT` | `8000` | Gunicorn portu (Render otomatik verir) |

## API örnekleri

```bash
BASE=http://localhost:8000

# F1: etkinlik oluştur
curl -s -X POST $BASE/api/events -H 'Content-Type: application/json' \
  -d '{"title":"Docker Atölyesi","location":"Lab 2","event_date":"2026-12-20T14:00","capacity":2}'

# F2: listele / ara / detay
curl -s "$BASE/api/events?q=docker"
curl -s $BASE/api/events/1

# F3: kayıt ol
curl -s -X POST $BASE/api/events/1/registrations -H 'Content-Type: application/json' \
  -d '{"full_name":"Ayşe Yılmaz","email":"ayse@ornek.com"}'

# F4: kontenjan doluysa HTTP 409 {"error":"capacity_full", ...}

# F5: kaydı iptal et
curl -s -X POST $BASE/api/events/1/registrations/cancel -H 'Content-Type: application/json' \
  -d '{"email":"ayse@ornek.com"}'

# İzleme
curl -s $BASE/health
curl -s $BASE/metrics
```

| Durum kodu | Anlamı |
|---|---|
| 200 / 201 | Başarılı / oluşturuldu |
| 400 `validation_error` | Eksik veya hatalı alan (`details` içinde alan bazlı mesajlar) |
| 404 `not_found` | Etkinlik veya kayıt bulunamadı |
| 409 `capacity_full` | Kontenjan dolu |
| 409 `duplicate_registration` | Bu e-posta bu etkinliğe zaten kayıtlı |

## DevOps süreci

```
feature/* ──PR──> CI (ruff + pytest + pip-audit + Docker build + konteyner smoke testi)
                   └─ yeşil ──merge──> main ──> CI (+ GHCR push)
                                                 └─ başarılı ──> CD: test edilen commit'i Render'a dağıt (ref=<sha>)
                                                                     → yeni sürümü bekle → canlı smoke test
                                                                     → başarısızsa önceki sürüme otomatik geri dön
```

| Bileşen | Dosya | Açıklama |
|---|---|---|
| Git akışı | [`docs/git-workflow.md`](docs/git-workflow.md) | Branch stratejisi, commit kuralları, haftalık branch planı |
| CI | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | PR'larda ve main'de: lint, birim testleri (%80 kapsam eşiği), pip-audit, Docker build + smoke test + commit doğrulama, GHCR |
| CD | [`.github/workflows/cd.yml`](.github/workflows/cd.yml), [`scripts/render_deploy.sh`](scripts/render_deploy.sh) | Yalnızca CI'dan geçen commit'i Render'a dağıtır; canlı smoke test, otomatik ve elle geri dönüş (rollback) |
| Docker | [`Dockerfile`](Dockerfile), [`docker-compose.yml`](docker-compose.yml) | Root olmayan kullanıcı, Gunicorn, HEALTHCHECK |
| Cloud | [`render.yaml`](render.yaml) | Render Blueprint (Docker, ücretsiz plan, `/health` kontrolü) |
| Monitoring | `/health`, `/metrics`, JSON loglar | Ayrıntılar: [`docs/deployment.md`](docs/deployment.md) |
| Kanban | [`kanban/`](kanban/README.md) | 31 kartlık 5 haftalık plan, GitHub Issues içe aktarma betiği |
| Bonus | [`k8s/`](k8s/README.md) | Minikube için Deployment + Service |

## Proje yapısı

```
├── app/
│   ├── __init__.py          # uygulama fabrikası, hata yöneticileri
│   ├── config.py            # ortam değişkenli yapılandırma
│   ├── db.py, schema.sql    # SQLite bağlantısı, şema, transaction
│   ├── services/            # iş kuralları (F1-F5), HTTP'den bağımsız
│   ├── routes/              # web (HTML), api (JSON), health (/health, /metrics)
│   ├── logging_config.py    # JSON loglar, request id, metrikler
│   ├── security.py          # CSRF, güvenlik başlıkları
│   ├── templates/, static/  # arayüz
│   └── seed.py              # demo verisi
├── tests/                   # pytest birim testleri
├── .github/workflows/       # ci.yml, cd.yml
├── Dockerfile, docker-compose.yml, render.yaml, gunicorn.conf.py
├── scripts/                 # smoke_test.sh, wait_for_deploy.sh
├── docs/                    # gereksinimler, mimari, git akışı, dağıtım, haftalık sunum notları
├── kanban/                  # Kanban planı, CSV, GitHub Issues betiği, haftalık snapshot'lar
├── teslim/                  # final rapor taslağı, Project_Links.txt, Evidence yapısı
└── k8s/                     # (bonus) Kubernetes manifestleri
```

## Bilinen sınırlamalar

- Render ücretsiz planında dosya sistemi kalıcı değil, bu yüzden SQLite verisi her deploy veya yeniden başlatmada
  sıfırlanıyor. Canlı demoda `SEED_DEMO_DATA=true` ile örnek veri yükleniyor. Kalıcı veri için Render Postgres ya da
  ücretli disk gerekir.
- Ücretsiz servis 15 dk trafik almazsa uyku moduna geçiyor; sonraki ilk istek yaklaşık 1 dakika sürebilir.
- Ders kapsamında kullanıcı girişi/yetkilendirme yok; kayıt iptali e-posta bilgisiyle yapılıyor.
