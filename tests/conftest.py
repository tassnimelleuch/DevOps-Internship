"""Pytest configuration for Flask tests."""
import pytest
from app import create_app
from app.models import db as _db

@pytest.fixture
def app():
    """Create test application."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    with app.app_context():
        _db.create_all()
    yield app
    with app.app_context():
        _db.drop_all()

@pytest.fixture
def client(app):
    """Test client for making requests."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """CLI test runner."""
    return app.test_cli_runner()