"""Unit tests for the Flask application."""
from app.app import create_app


def test_app_creation():
    """Test if the app instance is created correctly.
    
    Verifies:
        - App instance is not None
        - Default testing config is False
    """
    test_app = create_app()
    assert test_app is not None
    assert test_app.config['TESTING'] is False  # Default state


def test_debug_mode_config():
    """Test debug mode configuration.
    
    Verifies:
        - Debug mode is False in production config
    """
    test_app = create_app()
    assert test_app.config['DEBUG'] is False  # Should be False in production config
      