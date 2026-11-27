"""İzleme: /health."""

import logging

from flask import Blueprint, current_app, jsonify

from ..db import engine_name, get_db

health_bp = Blueprint("health", __name__)
logger = logging.getLogger(__name__)


@health_bp.get("/health")
def health():
    """Render ve Docker HEALTHCHECK kullanıyor. Veritabanına ulaşılamazsa 503."""
    cfg = current_app.config
    try:
        get_db().execute("SELECT 1").fetchone()
        database_ok = True
    except Exception as exc:
        database_ok = False
        logger.error("health_check_failed", extra={"error": str(exc)})
    body = {
        "status": "ok" if database_ok else "error",
        "checks": {"database": "ok" if database_ok else "error"},
        "database": engine_name(cfg["DATABASE_URL"]),
        "version": cfg["APP_VERSION"],
        "commit": cfg["GIT_SHA"],
        "environment": cfg["APP_ENV"],
        "uptime_seconds": current_app.extensions["metrics"].uptime_seconds(),
    }
    return jsonify(body), 200 if database_ok else 503
