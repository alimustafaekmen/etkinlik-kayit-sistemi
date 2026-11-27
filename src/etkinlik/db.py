"""Veritabanı bağlantısı. Yerelde SQLite, DATABASE_URL tanımlıysa PostgreSQL."""

import sqlite3
from contextlib import contextmanager
from pathlib import Path

import psycopg
from flask import Flask, current_app, g
from psycopg.rows import dict_row

SCHEMA_DIR = Path(__file__).parent


class PostgresConnection(psycopg.Connection):
    # Servislerde SQLite'taki gibi "?" kullanıyorum, psycopg ise "%s" bekliyor
    def execute(self, query, params=None, **kwargs):
        return super().execute(query.replace("?", "%s"), params, **kwargs)


Connection = sqlite3.Connection | PostgresConnection


def _dict_row(cursor, values):
    return {column[0]: value for column, value in zip(cursor.description, values, strict=True)}


def is_postgres(conn: Connection) -> bool:
    return isinstance(conn, PostgresConnection)


def engine_name(database_url: str) -> str:
    # Adres şifre içerdiği için loglarda sadece motor adı gösteriliyor
    return "postgresql" if database_url else "sqlite"


def connect(target: str) -> Connection:
    # İki motorda da autocommit açık, yazma işlemleri transaction() ile yapılıyor
    if "://" in target:  # yanlış yazılmış adres SQLite dosyası sanılmasın
        try:
            return PostgresConnection.connect(
                target, autocommit=True, row_factory=dict_row, connect_timeout=10
            )
        except psycopg.ProgrammingError:
            # psycopg'nin mesajında şifre görünebiliyor
            raise psycopg.ProgrammingError("DATABASE_URL geçersiz, biçimini kontrol edin.") from None

    Path(target).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(target, isolation_level=None, timeout=5)
    conn.row_factory = _dict_row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def transaction(conn: Connection):
    # SQLite'ta BEGIN IMMEDIATE yazma kilidini baştan alır, aynı anda gelen kayıtlar kontenjanı aşamaz.
    # PostgreSQL'de kilit serviste SELECT ... FOR UPDATE ile alınıyor.
    conn.execute("BEGIN" if is_postgres(conn) else "BEGIN IMMEDIATE")
    try:
        yield
        conn.execute("COMMIT")
    except BaseException:
        conn.execute("ROLLBACK")
        raise


def get_db() -> Connection:
    """İstek başına bir bağlantı."""
    if "db" not in g:
        g.db = connect(current_app.config["DATABASE_URL"] or current_app.config["DATABASE_PATH"])
    return g.db


def close_db(_exc=None) -> None:
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()


def init_schema(conn: Connection) -> None:
    """Tabloları yoksa oluşturur."""
    if is_postgres(conn):
        conn.execute((SCHEMA_DIR / "schema_postgres.sql").read_text(encoding="utf-8"))
    else:
        conn.executescript((SCHEMA_DIR / "schema.sql").read_text(encoding="utf-8"))


def init_app(app: Flask) -> None:
    app.teardown_appcontext(close_db)
    with app.app_context():
        conn = get_db()
        init_schema(conn)
        if app.config["SEED_DEMO_DATA"]:
            from .seed import seed_demo_data

            seed_demo_data(conn)
