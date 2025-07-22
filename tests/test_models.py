"""Test database models."""
from app.models import Task, db

def test_new_task(app):
    """Test task creation."""
    with app.app_context():
        task = Task(content="Test task", done=False)
        db.session.add(task)
        db.session.commit()
        
        assert task.id == 1
        assert task.content == "Test task"
        assert not task.done
        assert str(task) == "<Task 1: Test task>"