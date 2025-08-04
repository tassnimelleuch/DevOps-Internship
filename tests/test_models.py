"""Unit tests for Task model."""
import pytest
from app.models import db, Task
from flask import Flask
@pytest.fixture
def app():
    """Create and configure a new app instance for each test.
    
    Yields:
        Flask: Test application instance
    """
    test_app = Flask(__name__)
    test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    test_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    test_app.config['TESTING'] = True
# Disabling CSRF protection in tests is safe because:
# 1. Tests run in isolated environment
# 2. No actual browser requests are made
# 3. Test database is temporary
    test_app.config['WTF_CSRF_ENABLED'] = False # nosec B104
    db.init_app(test_app)
    with test_app.app_context():
        db.create_all()
        yield test_app
        db.session.remove()
        db.drop_all()
@pytest.fixture
def session(app):  # pylint: disable=redefined-outer-name
    """Provide a database session for testing.
    
    Args:
        app: Flask application fixture
        
    Yields:
        SQLAlchemy: Database session
    """
    with app.app_context():
        db.session.begin_nested()
        yield db.session
        db.session.rollback()
def test_task_creation(session):  # pylint: disable=redefined-outer-name
    """Test basic task creation.
    
    Verifies:
        - Task gets assigned an ID
        - Content is stored correctly
        - Done defaults to False
    """
    task = Task(content="Test Task")
    session.add(task)
    session.commit()
    assert task.id is not None
    assert task.content == "Test Task"
    assert task.done is False
def test_task_repr(session):  # pylint: disable=redefined-outer-name
    """Test task string representation.
    
    Verifies:
        - __repr__ returns expected format
    """
    task = Task(content="Sample Task")
    session.add(task)
    session.commit()
    assert repr(task) == "<Task Sample Task>"
def test_task_done_default(session):  # pylint: disable=redefined-outer-name
    """Test default done status.
    
    Verifies:
        - Done flag defaults to False
    """
    task = Task(content="Another Task")
    session.add(task)
    session.commit()
    assert not task.done
def test_update_task_done(session):  # pylint: disable=redefined-outer-name
    """Test updating task completion status.
    
    Verifies:
        - Done status can be updated
        - Changes persist in database
    """
    task = Task(content="Finish task")
    session.add(task)
    session.commit()
    task.done = True
    session.commit()
    updated_task = session.get(Task, task.id)
    assert updated_task.done is True
def test_task_content_nullable(session):  # pylint: disable=redefined-outer-name
    """Test content null constraint.
    
    Verifies:
        - Task cannot be created without content
    """
    with pytest.raises(ValueError):
        task = Task()
        session.add(task)
        session.commit()
