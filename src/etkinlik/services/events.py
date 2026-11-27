"""F1 etkinlik oluşturma."""

import logging
from datetime import datetime

from ..db import Connection
from ..errors import NotFoundError, ValidationError
from .validation import DATE_FORMAT, clean_text, local_now, parse_datetime, parse_int

logger = logging.getLogger(__name__)

MAX_CAPACITY = 10_000

# Doluluk için kayıtlı kişi sayısıyla birlikte okunuyor
EVENT_SELECT = """
    SELECT e.id, e.title, e.description, e.location, e.event_date, e.capacity, e.created_at,
           COUNT(r.id) AS registered_count
    FROM events e LEFT JOIN registrations r ON r.event_id = e.id
"""


def _with_occupancy(row: dict, now: datetime) -> dict:
    remaining = row["capacity"] - row["registered_count"]
    return {
        **row,
        "remaining_seats": max(remaining, 0),
        "is_full": remaining <= 0,
        "is_past": datetime.fromisoformat(row["event_date"]) < now,
    }


def validate_event(data: dict, now: datetime) -> dict:
    """Hatalı alanların hepsini tek ValidationError ile döndürür."""
    errors: dict[str, str] = {}
    cleaned = {
        "title": clean_text(data, "title", errors, label="Etkinlik adı", min_len=3, max_len=120),
        "description": clean_text(
            data, "description", errors, label="Açıklama", max_len=1000, required=False
        ),
        "location": clean_text(data, "location", errors, label="Konum", min_len=2, max_len=120),
        "capacity": parse_int(
            data.get("capacity"), "capacity", errors, label="Kontenjan", maximum=MAX_CAPACITY
        ),
    }
    event_date = parse_datetime(data.get("event_date"), "event_date", errors, label="Tarih")
    if event_date and event_date <= now:
        errors["event_date"] = "Etkinlik tarihi gelecekte olmalıdır."
    if errors:
        raise ValidationError("Etkinlik bilgileri geçersiz.", errors)
    return {**cleaned, "event_date": event_date.strftime(DATE_FORMAT)}


def create_event(conn: Connection, data: dict, now: datetime | None = None) -> dict:
    """F1: Yeni etkinlik oluşturur."""
    now = now or local_now()
    event = validate_event(data, now)
    row = conn.execute(
        "INSERT INTO events (title, description, location, event_date, capacity) "
        "VALUES (?, ?, ?, ?, ?) RETURNING id",
        (event["title"], event["description"], event["location"], event["event_date"], event["capacity"]),
    ).fetchone()
    logger.info("event_created", extra={"event_id": row["id"], "capacity": event["capacity"]})
    return get_event(conn, row["id"], now)


def get_event(conn: Connection, event_id: int, now: datetime | None = None) -> dict:
    """F2: Etkinlik detayı."""
    row = conn.execute(EVENT_SELECT + " WHERE e.id = ? GROUP BY e.id", (event_id,)).fetchone()
    if row is None:
        raise NotFoundError(f"Etkinlik bulunamadı (id={event_id}).")
    return _with_occupancy(row, now or local_now())
