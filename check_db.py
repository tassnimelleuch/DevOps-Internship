#!/usr/bin/env python3
"""Database checker for Flask Todo App."""
from app import create_app, db
from app.models import Task
def check_database():
    """Check database contents and display task information.
    Performs:
        - Database connection check
        - Table creation verification
        - Task listing with status
        - Completion statistics
    """
    print("=" * 50)
    print("DATABASE CHECK")
    print("=" * 50)
    app = create_app()
    with app.app_context():
        # Verify database tables
        db.create_all()
        print("✅ Database tables created!")
        # Query all tasks
        tasks = Task.query.all()
        print(f"📊 Total tasks: {len(tasks)}")
        done_tasks = 0
        pending_tasks = 0
        if tasks:
            print("\n📋 Task details:")
            for task in tasks:
                status = "✓ Done" if task.done else "○ Pending"
                print(f"   ID: {task.id:2d} | {status} | {task.content}")
            done_tasks = Task.query.filter_by(done=True).count()
            pending_tasks = Task.query.filter_by(done=False).count()
        else:
            print("\n📝 No tasks found in the database.")
            print("   💡 Try adding some tasks through the web interface!")
        print("\n📈 Statistics:")
        print(f"   ✓ Completed tasks: {done_tasks}")
        print(f"   ○ Pending tasks: {pending_tasks}")
    print("\n📁 Database location: app/instance/app.db")
if __name__ == "__main__":
    check_database()
