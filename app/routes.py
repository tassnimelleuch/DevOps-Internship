from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Task
from app.summarize import get_summary 

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Display all tasks."""
    tasks = db.session.execute(db.select(Task)).scalars().all()  # Modern SQLAlchemy 2.0 query
    return render_template('index.html', tasks=tasks)

@bp.route('/add', methods=['POST'])
def add():
    """Add a new task."""
    task_content = request.form['content']
    if task_content.strip():  # Basic validation
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    """Display edit form for a task."""
    task = db.session.get(Task, id)  # Modern session.get() instead of query.get()
    if not task:
        abort(404)
    return render_template('edit.html', task=task)

@bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    """Update an existing task."""
    task = db.session.get(Task, id)
    if not task:
        abort(404)
    task.content = request.form['content']
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:id>')
def delete(id):
    """Delete a task."""
    task = db.session.get(Task, id)
    if not task:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/toggle/<int:id>')
def toggle(id):
    """Toggle the done status of a task."""
    task = db.session.get(Task, id)
    if not task:
        abort(404)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('main.index'))
    
@bp.route('/summarize', methods=['POST'])
def summarize():
    """Handle text summarization requests."""
    if request.is_json:
        text = request.json.get('text')
    else:
        text = request.form.get('text')
    
    if not text or not text.strip():
        return jsonify({"error": "No text provided"}), 400
    
    try:
        summary = get_summary(text)
        if request.is_json:
            return jsonify({"summary": summary})
        return render_template('index.html', summary=summary)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')