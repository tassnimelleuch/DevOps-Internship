import os


class Config:
    # This MUST match exactly
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.path.dirname(__file__), 'instance', 'app.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    base_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'instance', 'app.db')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Add production database URI here
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 