from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Task

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Display all tasks."""
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add', methods=['POST'])
def add():
    """Add a new task."""
    task_content = request.form['content']
    if task_content.strip():  # Basic validation
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))  # Fixed: added 'main.' prefix

@bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    """Display edit form for a task."""
    task = Task.query.get_or_404(id)
    return render_template('edit.html', task=task)

@bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    """Update an existing task."""
    task = Task.query.get_or_404(id)
    task.content = request.form['content']
    db.session.commit()
    return redirect(url_for('main.index'))  # Fixed: added 'main.' prefix

@bp.route('/delete/<int:id>')
def delete(id):
    """Delete a task."""
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('main.index'))  # Fixed: added 'main.' prefix

@bp.route('/toggle/<int:id>')
def toggle(id):
    """Toggle the done status of a task."""
    task = Task.query.get_or_404(id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('main.index'))  # Fixed: added 'main.' prefix