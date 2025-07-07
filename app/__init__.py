from flask import Flask
from .models import db
from .config import Config  # CHANGED THIS LINE
from flask import Flask
from .config import Config
from .models import db
from .summarize import bp as summarize_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # Import and register blueprints
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    from .summarize import bp as summarize_bp
    app.register_blueprint(summarize_bp, url_prefix='/summarize')
    
    return app