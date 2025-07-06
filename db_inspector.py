#!/usr/bin/env python3
"""
Comprehensive database inspector for Flask Todo App
"""

import sqlite3
import os
import sys

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app import create_app
from app.models import Task

def check_with_sqlite():
    """Check database using direct SQLite connection"""
    print("=" * 60)
    print("DATABASE INSPECTION USING SQLITE")
    print("=" * 60)
    
    db_path = os.path.join('app', 'instance', 'app.db')
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found at: {db_path}")
        return
    
    print(f"✅ Database file found at: {db_path}")
    print(f"📁 File size: {os.path.getsize(db_path)} bytes")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Show all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print(f"\n📋 Tables in database: {len(tables)}")
    for table in tables:
        print(f"   - {table[0]}")
    
    # Show task table schema
    if ('task',) in tables:
        print(f"\n🔍 Task table schema:")
        cursor.execute("PRAGMA table_info(task);")
        columns = cursor.fetchall()
        for col in columns:
            nullable = "NOT NULL" if col[3] else "NULL"
            default = f"Default: {col[4]}" if col[4] else "No default"
            print(f"   - {col[1]} ({col[2]}) - {nullable} - {default}")
    
    # Show task data
    if ('task',) in tables:
        cursor.execute("SELECT * FROM task;")
        tasks = cursor.fetchall()
        
        print(f"\n📝 Task data ({len(tasks)} records):")
        if tasks:
            for task in tasks:
                status = "✓ Done" if task[2] else "○ Pending"
                print(f"   ID: {task[0]:2d} | {status} | '{task[1]}'")
        else:
            print("   No tasks found.")
    
    conn.close()

def check_with_flask():
    """Check database using Flask-SQLAlchemy"""
    print("\n" + "=" * 60)
    print("DATABASE INSPECTION USING FLASK-SQLALCHEMY")
    print("=" * 60)
    
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
        
        # Show some statistics
        done_tasks = Task.query.filter_by(done=True).count()
        pending_tasks = Task.query.filter_by(done=False).count()
        
        print(f"\n📈 Statistics:")
        print(f"   ✓ Completed tasks: {done_tasks}")
        print(f"   ○ Pending tasks: {pending_tasks}")

def show_commands():
    """Show useful commands for database management"""
    print("\n" + "=" * 60)
    print("USEFUL COMMANDS FOR DATABASE MANAGEMENT")
    print("=" * 60)
    
    print("🔧 SQLite Command Line:")
    print("   sqlite3 app/instance/app.db")
    print("   .tables                    # Show all tables")
    print("   .schema task              # Show task table schema")
    print("   SELECT * FROM task;       # Show all tasks")
    print("   .quit                     # Exit SQLite")
    
    print("\n🐍 Python Commands:")
    print("   python check_db_simple.py  # Quick database check")
    print("   python db_inspector.py     # Comprehensive inspection")
    
    print("\n🌐 Web Interface:")
    print("   python run.py             # Start the web server")
    print("   Then visit: http://localhost:5000")

if __name__ == "__main__":
    check_with_sqlite()
    check_with_flask()
    show_commands() 