import pytest
from app.models import db, Task
from flask import Flask

# filepath: c:\Users\TASNIM\Desktop\FLASKAPP\DevOps-Internship\tests\test_models.py


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def session(app):
    with app.app_context():
        yield db.session

def test_task_creation(session):
    task = Task(content="Test Task")
    session.add(task)
    session.commit()
    assert task.id is not None
    assert task.content == "Test Task"
    assert task.done is False

def test_task_repr(session):
    task = Task(content="Sample Task")
    session.add(task)
    session.commit()
    assert repr(task) == "<Task Sample Task>"

def test_task_done_default(session):
    task = Task(content="Another Task")
    session.add(task)
    session.commit()
    assert not task.done

def test_update_task_done(session):
    task = Task(content="Finish task")
    session.add(task)
    session.commit()
    task.done = True
    session.commit()
    updated_task = Task.query.get(task.id)
    assert updated_task.done is True

def test_task_content_nullable(session):
    with pytest.raises(Exception):
        task = Task()
        session.add(task)
        session.commit()