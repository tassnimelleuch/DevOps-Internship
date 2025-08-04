"""testing routes"""
from unittest.mock import patch
import pytest # type: ignore
from app import create_app, db



@pytest.fixture
def app():
    """Create test app with isolated database"""
    app = create_app() # pylint: disable=redefined-outer-name
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

    with app.app_context():
        db.create_all()  # Create tables for tests
        yield app
        db.drop_all()  # Cleanup
# Route Tests
def test_index_route(client): # pylint: disable=redefined-outer-name
    """Test the index route returns 200 and contains 'TaskFlow'."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'TaskFlow' in response.data

def test_add_task(client): # pylint: disable=redefined-outer-name
    """Test adding a new task via POST and verify it appears."""
    response = client.post('/add',  # pylint: disable=redefined-outer-name
                         data={'content': 'New Task'},
                         follow_redirects=True)
    assert response.status_code == 200
    assert b'New Task' in response.data  # Verify task appears

def test_edit_route(client, test_task): # pylint: disable=redefined-outer-name
    """Test editing a task loads the correct content."""
    response = client.get(f'/edit/{test_task.id}')
    assert response.status_code == 200
    assert b'Test task' in response.data  # Verify task loads

def test_update_route(client, test_task): # pylint: disable=redefined-outer-name
    """Test updating a task via POST and verify changes."""
    response = client.post(f'/update/{test_task.id}', # pylint: disable=redefined-outer-name
                         data={'content': 'Updated'},
                         follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated' in response.data

def test_delete_route(client, test_task): # pylint: disable=redefined-outer-name
    """Test deleting a task and verify it is removed."""
    response = client.get(f'/delete/{test_task.id}',
                        follow_redirects=True)
    assert response.status_code == 200
    assert b'Test task' not in response.data  # Verify deletion

def test_toggle_route(client, test_task): # pylint: disable=redefined-outer-name
    """Test toggling a task's done status."""
    initial_state = test_task.done
    response = client.get(f'/toggle/{test_task.id}', # pylint: disable=redefined-outer-name
                        follow_redirects=True)
    assert response.status_code == 200
    assert test_task.done != initial_state  # Verify toggle

def test_summarize_json(client): # pylint: disable=redefined-outer-name
    """Test summarization endpoint with JSON input."""
    with patch('app.routes.get_summary', return_value="Mocked summary"):
        response = client.post('/summarize',
                            json={'text': 'Test text'},
                            headers={'Content-Type': 'application/json'})
        assert response.status_code == 200
        assert response.json['summary'] == "Mocked summary"

def test_pomodoro_route(client): # pylint: disable=redefined-outer-name
    """Test the pomodoro route returns 200 and contains 'Pomodoro'."""
    response = client.get('/pomodoro')
    assert response.status_code == 200
    assert b'Pomodoro' in response.data
