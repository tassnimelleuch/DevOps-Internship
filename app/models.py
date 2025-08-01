# pylint: disable=too-few-public-methods
"""Database models for the task management system."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    """Task model representing todo items in the database.

    Attributes:
        id: Primary key integer ID.
        content: Task description (max 200 chars).
        done: Completion status (defaults to False).
    """
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        """Return string representation of the task.
        
        Returns:
            str: Format '<Task {content}>'
        """
        return f'<Task {self.content}>'
    