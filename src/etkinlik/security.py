"""Formlar için CSRF koruması."""

import secrets

from flask import Flask, request, session

from .errors import ValidationError


def csrf_token() -> str:
    """Formlara gizli alan olarak eklenen, oturuma bağlı token."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_urlsafe(32)
    return session["csrf_token"]


def init_security(app: Flask) -> None:
    app.jinja_env.globals["csrf_token"] = csrf_token

    @app.before_request
    def _check_csrf() -> None:
        # Sadece web formları. JSON API application/json istediği için başka sitedeki form tetikleyemez.
        if not app.config["CSRF_ENABLED"] or request.method != "POST" or request.blueprint != "web":
            return
        expected = session.get("csrf_token", "")
        sent = request.form.get("csrf_token", "")
        # compare_digest ASCII olmayan str'de hata veriyor, bytes karşılaştırıyorum
        if not expected or not secrets.compare_digest(expected.encode(), sent.encode()):
            raise ValidationError("Geçersiz veya süresi dolmuş form. Sayfayı yenileyip tekrar deneyin.")
