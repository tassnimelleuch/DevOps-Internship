"""Flask application factory module."""

from flask import Flask
from .config import Config
from .models import db
def create_app() -> Flask:
    """Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import and register blueprints
    from .routes import \
        bp as main_bp  # pylint: disable=import-outside-toplevel
    from .summarize import \
        bp as summarize_bp  # pylint: disable=import-outside-toplevel

    app.register_blueprint(main_bp)
    app.register_blueprint(summarize_bp, url_prefix="/summarize")

    return app
