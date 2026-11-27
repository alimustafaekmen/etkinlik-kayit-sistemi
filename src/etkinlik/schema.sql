-- Veri modeli (SQLite): events 1 - N registrations

CREATE TABLE IF NOT EXISTS events (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    description TEXT    NOT NULL DEFAULT '',
    location    TEXT    NOT NULL,
    event_date  TEXT    NOT NULL,                        -- ISO 8601: YYYY-MM-DDTHH:MM
    capacity    INTEGER NOT NULL CHECK (capacity > 0),
    created_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

CREATE TABLE IF NOT EXISTS registrations (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id      INTEGER NOT NULL REFERENCES events (id) ON DELETE CASCADE,
    full_name     TEXT    NOT NULL,
    email         TEXT    NOT NULL,                      -- küçük harfe çevrilmiş olarak saklanır
    registered_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    UNIQUE (event_id, email)                             -- aynı e-posta aynı etkinliğe bir kez kaydolur
);

CREATE INDEX IF NOT EXISTS idx_registrations_event_id ON registrations (event_id);
CREATE INDEX IF NOT EXISTS idx_events_event_date ON events (event_date);
