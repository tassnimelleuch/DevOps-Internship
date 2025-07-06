#!/usr/bin/env python3
"""
Simple script to check the database using Flask-SQLAlchemy
"""

import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app import create_app
from app.models import Task

def check_database():
    # Create the Flask app
    app = create_app()
    
    # Use the application context
    with app.app_context():
        # Get all tasks
        tasks = Task.query.all()
        
        print(f"Database check for Flask Todo App")
        print("=" * 50)
        print(f"Total tasks in database: {len(tasks)}")
        print()
        
        if tasks:
            print("Task details:")
            for task in tasks:
                status = "✓ Done" if task.done else "○ Pending"
                print(f"  ID: {task.id:2d} | {status} | {task.content}")
        else:
            print("No tasks found in the database.")
            print("Try adding some tasks through the web interface!")
        
        print()
        print("Database location: app/instance/app.db")

if __name__ == "__main__":
    check_database() 