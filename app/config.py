import os

class Config:
    """Base configuration class."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

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