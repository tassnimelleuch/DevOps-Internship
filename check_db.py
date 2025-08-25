#!/usr/bin/env python3
"""Database checker for Flask Todo App."""
import os
from app import create_app, db
from app.models import Task

def check_database():
    """Check database contents and display task information.
    Performs:
        - Database existence check
        - Task listing with status
        - Completion statistics
    """
    print("=" * 50)
    print("DATABASE CHECK")
    print("=" * 50)

    app = create_app()
    db_path = os.path.join(app.instance_path, "app.db")

    if not os.path.exists(db_path):
        print("❌ Database not found!")
        print("💡 Start the app first to create the database automatically.")
        return

    with app.app_context():
        # Query all tasks
        tasks = Task.query.all()
        print(f"📊 Total tasks: {len(tasks)}")

        done_tasks = Task.query.filter_by(done=True).count()
        pending_tasks = Task.query.filter_by(done=False).count()

        if tasks:
            print("\n📋 Task details:")
            for task in tasks:
                status = "✓ Done" if task.done else "○ Pending"
                print(f"   ID: {task.id:2d} | {status} | {task.content}")
        else:
            print("\n📝 No tasks found in the database.")
            print("   💡 Try adding some tasks through the web interface!")

        print("\n📈 Statistics:")
        print(f"   ✓ Completed tasks: {done_tasks}")
        print(f"   ○ Pending tasks: {pending_tasks}")

    print("\n📁 Database location:", db_path)

if __name__ == "__main__":
    check_database()
