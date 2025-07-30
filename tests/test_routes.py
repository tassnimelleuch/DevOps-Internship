import pytest
from app import create_app, db
from app.models import Task
from unittest.mock import patch


@pytest.fixture
def app():
    """Create test app with isolated database"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

    with app.app_context():
        db.create_all()  # Create tables for tests
        yield app
        db.drop_all()  # Cleanup

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_task(app):
    with app.app_context():
        task = Task(content="Test task")
        db.session.add(task)
        db.session.commit()
        yield task
        # Add this check before deletion:
        if task in db.session:  # Only delete if still exists
            db.session.delete(task)
            db.session.commit()
# Route Tests
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'TaskFlow' in response.data  

def test_add_task(client):
    response = client.post('/add', 
                         data={'content': 'New Task'},
                         follow_redirects=True)
    assert response.status_code == 200
    assert b'New Task' in response.data  # Verify task appears

def test_edit_route(client, test_task):
    response = client.get(f'/edit/{test_task.id}')
    assert response.status_code == 200
    assert b'Test task' in response.data  # Verify task loads

def test_update_route(client, test_task):
    response = client.post(f'/update/{test_task.id}',
                         data={'content': 'Updated'},
                         follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated' in response.data

def test_delete_route(client, test_task):
    response = client.get(f'/delete/{test_task.id}', 
                        follow_redirects=True)
    assert response.status_code == 200
    assert b'Test task' not in response.data  # Verify deletion

def test_toggle_route(client, test_task):
    initial_state = test_task.done
    response = client.get(f'/toggle/{test_task.id}',
                        follow_redirects=True)
    assert response.status_code == 200
    assert test_task.done != initial_state  # Verify toggle

def test_summarize_json(client):
    with patch('app.routes.get_summary', return_value="Mocked summary"):
        response = client.post('/summarize',
                            json={'text': 'Test text'},
                            headers={'Content-Type': 'application/json'})
        assert response.status_code == 200
        assert response.json['summary'] == "Mocked summary"

def test_pomodoro_route(client):
    response = client.get('/pomodoro')
    assert response.status_code == 200
    assert b'Pomodoro' in response.data