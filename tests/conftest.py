import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    
    # Push application context
    with app.app_context():
        db.create_all()  # Create all tables
        yield app
        db.drop_all()  # Clean up

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def test_task(app):
    """Create a test task in the database."""
    with app.app_context():
        task = Task(content="Test task")
        db.session.add(task)
        db.session.commit()
        yield task
        db.session.delete(task)
        db.session.commit()