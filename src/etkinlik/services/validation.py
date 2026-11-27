"""Girdi doğrulama. Hatalar `errors` sözlüğüne alan adıyla yazılır."""

import re
from datetime import datetime
from zoneinfo import ZoneInfo

from ..config import Config

TIMEZONE = ZoneInfo(Config.APP_TIMEZONE)
DATE_FORMAT = "%Y-%m-%dT%H:%M"  # HTML datetime-local biçimi
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)*\.[a-z]{2,}")


def local_now() -> datetime:
    """Uygulama saat dilimine göre şu an (dakika hassasiyetinde)."""
    return datetime.now(TIMEZONE).replace(tzinfo=None, second=0, microsecond=0)


def clean_text(
    data: dict, field: str, errors: dict, *, label: str, min_len=0, max_len=200, required=True
) -> str:
    value = data.get(field) or ""
    if not isinstance(value, str):  # JSON'dan sayı veya liste gelebilir
        errors[field] = f"{label} metin olmalıdır."
        return ""
    value = value.strip()
    if required and not value:
        errors[field] = f"{label} zorunludur."
    elif value and len(value) < min_len:
        errors[field] = f"{label} en az {min_len} karakter olmalıdır."
    elif len(value) > max_len:
        errors[field] = f"{label} en fazla {max_len} karakter olabilir."
    return value


def parse_datetime(value, field: str, errors: dict, *, label: str) -> datetime | None:
    if not value:
        errors[field] = f"{label} zorunludur."
        return None
    try:
        parsed = datetime.fromisoformat(str(value).strip())
    except ValueError:
        errors[field] = f"{label} geçerli bir tarih olmalıdır (ör. 2026-12-12T19:00)."
        return None
    return parsed.replace(tzinfo=None, second=0, microsecond=0)


def parse_int(value, field: str, errors: dict, *, label: str, maximum: int) -> int | None:
    text = "" if value is None else str(value).strip()
    if not text:
        errors[field] = f"{label} zorunludur."
        return None
    try:
        number = int(text)
    except ValueError:
        errors[field] = f"{label} tam sayı olmalıdır."
        return None
    if not 1 <= number <= maximum:
        errors[field] = f"{label} 1 ile {maximum} arasında olmalıdır."
        return None
    return number


def clean_email(value, errors: dict) -> str:
    """Küçük harfe çevirir (Ali@X.com = ali@x.com) ve biçimi kontrol eder."""
    email = str(value or "").strip().lower()
    if not email:
        errors["email"] = "E-posta zorunludur."
    elif len(email) > 254 or not EMAIL_RE.fullmatch(email):
        errors["email"] = "Geçerli bir e-posta adresi giriniz."
    return email


def mask_email(email: str) -> str:
    """ali.veli@ornek.com -> al***@ornek.com"""
    local, _, domain = email.partition("@")
    return f"{local[:2] if len(local) > 2 else local[:1]}***@{domain}"
