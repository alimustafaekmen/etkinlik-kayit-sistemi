"""Flask uygulama fabrikası."""

from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

from . import db
from .config import Config
from .errors import ServiceError
from .logging_config import init_logging
from .security import init_security


def create_app(config_overrides: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.update(config_overrides or {})
    app.json.ensure_ascii = False  # Türkçe karakterler bozulmasın
    app.json.compact = True

    if app.config["APP_ENV"] == "production":
        # Render proxy arkasında, gerçek istemci IP'si X-Forwarded-For'da
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

    init_logging(app)
    init_security(app)
    db.init_app(app)

    @app.errorhandler(ServiceError)
    def handle_service_error(exc: ServiceError):
        return jsonify(exc.to_dict()), exc.status_code

    from .routes import BLUEPRINTS

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
    return app
