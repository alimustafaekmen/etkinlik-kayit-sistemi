"""REST API (JSON)."""

from flask import Blueprint, jsonify, request

from .. import services
from ..db import get_db
from ..errors import ValidationError

api_bp = Blueprint("api", __name__, url_prefix="/api")


def _json_body() -> dict:
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        raise ValidationError("İstek gövdesi JSON nesnesi olmalıdır (Content-Type: application/json).")
    return data


@api_bp.post("/events")
def create_event():
    """F1: POST /api/events  {title, location, event_date, capacity, description?}"""
    event = services.create_event(get_db(), _json_body())
    return jsonify(event=event), 201
