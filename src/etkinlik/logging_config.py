"""JSON loglar, istek kimliği (X-Request-ID) ve basit istek metrikleri."""

import json
import logging
import sys
import threading
import time
import uuid
from collections import Counter
from datetime import UTC, datetime

from flask import Flask, g, request

# LogRecord'un kendi alanları, geri kalanlar extra={...} ile geliyor
_RECORD_KEYS = set(vars(logging.makeLogRecord({}))) | {"message", "asctime"}
_QUIET_PATHS = ("/health", "/static/")  # sık health check'ler logu doldurmasın

logger = logging.getLogger("etkinlik.http")


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(timespec="milliseconds"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        payload.update({k: v for k, v in vars(record).items() if k not in _RECORD_KEYS})
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False, default=str)


class Metrics:
    """/metrics için istek sayaçları."""

    def __init__(self) -> None:
        self.started_at = time.time()
        self.counts: Counter[str] = Counter()
        self.total_ms = 0.0
        self._lock = threading.Lock()  # gunicorn thread'leri aynı sayacı kullanıyor

    def record(self, status: int, duration_ms: float) -> None:
        with self._lock:
            self.counts[f"{status // 100}xx"] += 1
            self.total_ms += duration_ms

    def snapshot(self) -> dict:
        with self._lock:
            total = sum(self.counts.values())
            return {
                "requests_total": total,
                "responses_by_status": dict(self.counts),
                "avg_response_ms": round(self.total_ms / total, 2) if total else 0.0,
            }

    def uptime_seconds(self) -> int:
        return int(time.time() - self.started_at)


def init_logging(app: Flask) -> None:
    root = logging.getLogger()
    # Testlerde create_app tekrar çağrılınca handler çoğalmasın
    if not any(isinstance(h.formatter, JsonFormatter) for h in root.handlers):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        root.addHandler(handler)
    root.setLevel(app.config["LOG_LEVEL"])
    logging.getLogger("werkzeug").setLevel(logging.WARNING)  # istek logunu kendimiz yazıyoruz

    metrics = app.extensions["metrics"] = Metrics()

    @app.before_request
    def _start_request() -> None:
        g.started = time.perf_counter()
        g.request_id = uuid.uuid4().hex[:12]

    @app.after_request
    def _log_request(response):
        duration_ms = round((time.perf_counter() - g.started) * 1000, 2)
        response.headers["X-Request-ID"] = g.request_id
        quiet = request.path.startswith(_QUIET_PATHS)
        if not quiet:
            metrics.record(response.status_code, duration_ms)
        if response.status_code >= 500:
            level = logging.ERROR
        elif response.status_code >= 400:
            level = logging.WARNING
        else:
            level = logging.DEBUG if quiet else logging.INFO
        logger.log(
            level,
            "http_request",
            extra={
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration_ms": duration_ms,
                "request_id": g.request_id,
                "remote_addr": request.remote_addr,
            },
        )
        return response
