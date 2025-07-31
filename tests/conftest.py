import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for testing."""
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

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

@pytest.fixture
def mock_summarizer():
    """Mock the summarizer function for testing."""
    with patch('app.services.summarizer.get_summary') as mock:
        mock.return_value = "Mocked summary"
        yield mock