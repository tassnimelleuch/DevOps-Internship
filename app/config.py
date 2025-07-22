"""Application configuration settings.

This module defines environment-specific configurations for:
- Database connections
- Security settings
- Flask application behavior
"""

import os
from typing import Dict, Type


class Config:
    """Base configuration with settings common to all environments."""

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///" + os.path.join(
        os.path.dirname(__file__), "instance", "app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SECRET_KEY: str = os.environ.get("SECRET_KEY") or "dev-secret-key"  # New
    PREFERRED_URL_SCHEME: str = "https"  # New
    def __init__(self):
        pass  # Dummy method


class DevelopmentConfig(Config):
    """Development-specific configuration with debug settings."""

    DEBUG: bool = True
    TESTING: bool = True  # New
    SQLALCHEMY_ECHO: bool = True  # New - logs SQL queries
    def __init__(self):
        pass  # Dummy method


class ProductionConfig(Config):
    """Production environment configuration with security optimizations."""

    DEBUG: bool = False
    SESSION_COOKIE_SECURE: bool = True  # New
    SESSION_COOKIE_HTTPONLY: bool = True  # New
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(os.path.dirname(__file__), "instance", "prod.db")
    def __init__(self):
        pass  # Dummy method


# Type hint for better IDE support
config: Dict[str, Type[Config]] = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
