#!/usr/bin/env python3
"""
Database checker for Flask Todo App
"""

import os
import sys

from app import create_app
from app.models import Task

sys.path.append(os.path.join(os.path.dirname(__file__), "app"))


def check_database():
    """Check database contents"""
    print("=" * 50)
    print("DATABASE CHECK")
    print("=" * 50)

    # Check with Flask-SQLAlchemy
    app = create_app()

    with app.app_context():
        tasks = Task.query.all()

        print(f"📊 Total tasks: {len(tasks)}")

        if tasks:
            print("\n📋 Task details:")
            for task in tasks:
                status = "✓ Done" if task.done else "○ Pending"
                print(f"   ID: {task.id:2d} | {status} | {task.content}")
        else:
            print("\n📝 No tasks found in the database.")
            print("   💡 Try adding some tasks through the web interface!")

        # Show statistics
        done_tasks = Task.query.filter_by(done=True).count()
        pending_tasks = Task.query.filter_by(done=False).count()

        print("\n📈 Statistics:")
        print(f"   ✓ Completed tasks: {done_tasks}")
        print(f"   ○ Pending tasks: {pending_tasks}")

    print(f"\n📁 Database location: app/instance/app.db")


if __name__ == "__main__":
    check_database()
