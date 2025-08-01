import pytest
from app.app import app, create_app

def test_app_creation():
    """Test if the app instance is created correctly"""
    test_app = create_app()
    assert test_app is not None
    assert test_app.config['TESTING'] is False  # Default state

def test_debug_mode_config():
    """Test debug mode configuration"""
    test_app = create_app()
    # Should be False in production config
    assert test_app.config['DEBUG'] is False  

def test_app_run_condition():
    """Test the __main__ condition"""
    assert __name__ != '__main__'