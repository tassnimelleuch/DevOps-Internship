from flask import Flask
from .models import db
from .config import config
from .routes import init_routes

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Initialize routes
    init_routes(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app 