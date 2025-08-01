"""Flask application factory module."""
from flask import Flask
from .config import Config
from .models import db
from .routes import bp as main_bp
from .summarize import bp as summarize_bp


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(summarize_bp, url_prefix='/summarize')

    return app
