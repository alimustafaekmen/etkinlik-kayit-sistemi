"""Uygulama ayarları. Değerler ortam değişkenlerinden okunur."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # proje kökü


def _git_sha() -> str:
    # Docker build'de GIT_SHA verilir, Render ise RENDER_GIT_COMMIT'i kendisi tanımlar
    for name in ("GIT_SHA", "RENDER_GIT_COMMIT"):
        value = os.environ.get(name, "")
        if value and value != "unknown":
            return value
    return "unknown"


class Config:
    APP_NAME = "Etkinlik Kayıt Sistemi"
    APP_VERSION = "1.0.0"
    APP_ENV = os.environ.get("APP_ENV", "development")
    APP_TIMEZONE = os.environ.get("APP_TIMEZONE", "Europe/Istanbul")
    GIT_SHA = _git_sha()
    REPO_URL = "https://github.com/alimustafaekmen/etkinlik-kayit-sistemi"

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-degistirin")
    DATABASE_PATH = os.environ.get("DATABASE_PATH", str(BASE_DIR / "data" / "events.db"))
    # Tanımlıysa SQLite yerine PostgreSQL kullanılır (canlıda Neon)
    DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
    SEED_DEMO_DATA = os.environ.get("SEED_DEMO_DATA", "").lower() == "true"

    CSRF_ENABLED = True  # testlerde kapatılıyor
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = APP_ENV == "production"  # canlıda çerez sadece HTTPS ile gider
    MAX_CONTENT_LENGTH = 64 * 1024  # 64 KB'tan büyük istek 413 alır
