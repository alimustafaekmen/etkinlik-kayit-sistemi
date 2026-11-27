from .api import api_bp
from .health import health_bp

BLUEPRINTS = [health_bp, api_bp]
