"""Database models for the Todo application with timestamp tracking."""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

db = SQLAlchemy()


class Task(db.Model):
    """Task model for storing todo items with completion status.

    Attributes:
        id (int): Primary key
        content (str): Task description text (200 char max)
        done (bool): Completion status flag
        created_at (datetime): When task was created
        updated_at (datetime): When task was last modified
    """

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # New
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow  # New
    )

    def __repr__(self) -> str:
        """Compact string representation for debugging.

        Returns:
            str: Formatted task ID and truncated content
        """
        return f'<Task {self.id}: {self.content[:20]}{"..." if len(self.content) > 20 else ""}>'

    def to_dict(self) -> dict:
        """Convert task to dictionary for JSON serialization.

        Returns:
            dict: Task data in key-value format
        """
        return {
            "id": self.id,
            "content": self.content,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


@event.listens_for(Task.content, "set")
def validate_content(target: Task, value: str, *args) -> None:
    """Validate task content before saving.

    Args:
        target: The Task instance being modified
        value: New content value
    Raises:
        ValueError: If content is empty or whitespace
    """
    if not value or not value.strip():
        raise ValueError("Task content cannot be empty")
