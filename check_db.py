#!/usr/bin/env python3
"""
Simple script to check the SQLite database contents
"""

import sqlite3
import os

def check_database():
    # Path to the database file
    db_path = os.path.join('app', 'instance', 'app.db')
    
    if not os.path.exists(db_path):
        print(f"Database file not found at: {db_path}")
        return
    
    print(f"Database file found at: {db_path}")
    print(f"File size: {os.path.getsize(db_path)} bytes")
    print("-" * 50)
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get table information
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")
    
    print("-" * 50)
    
    # Check the task table
    if ('task',) in tables:
        print("Task table contents:")
        cursor.execute("SELECT * FROM task;")
        tasks = cursor.fetchall()
        
        if tasks:
            print(f"Total tasks: {len(tasks)}")
            print("\nTask details:")
            for task in tasks:
                print(f"  ID: {task[0]}, Content: '{task[1]}', Done: {task[2]}")
        else:
            print("No tasks found in the database.")
    else:
        print("Task table not found.")
    
    # Show table schema
    print("-" * 50)
    print("Task table schema:")
    cursor.execute("PRAGMA table_info(task);")
    columns = cursor.fetchall()
    for col in columns:
        print(f"  {col[1]} ({col[2]}) - {'NOT NULL' if col[3] else 'NULL'} - Default: {col[4]}")
    
    conn.close()

if __name__ == "__main__":
    check_database() 