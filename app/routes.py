"""Flask routes for the task management application.

This module handles all web routes including:
- Task CRUD operations (Create, Read, Update, Delete)
- Text summarization endpoint
- Pomodoro timer page
"""
from flask import (Blueprint, jsonify, redirect, render_template, request,
                  url_for)
from .models import Task, db
from .services.summarizer import get_summary

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Display all tasks.
    
    Returns:
        Rendered template with all tasks from database.
    """
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@bp.route("/add", methods=["POST"])
def add():
    """Add a new task to the database.
    
    Returns:
        Redirect to index page after adding task.
        
    Notes:
        Only adds task if content is non-empty after stripping whitespace.
    """
    task_content = request.form["content"]
    if task_content.strip():
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/edit/<int:task_id>", methods=["GET"])
def edit(task_id):
    """Display edit form for a specific task.
    
    Args:
        task_id: Primary key of task to edit.
        
    Returns:
        Rendered edit template with task data.
        
    Raises:
        404: If task doesn't exist.
    """
    task = Task.query.get_or_404(task_id)
    return render_template("edit.html", task=task)


@bp.route("/update/<int:task_id>", methods=["POST"])
def update(task_id):
    """Update content of an existing task.
    
    Args:
        task_id: Primary key of task to update.
        
    Returns:
        Redirect to index page after update.
    """
    task = Task.query.get_or_404(task_id)
    task.content = request.form["content"]
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/delete/<int:task_id>")
def delete(task_id):
    """Permanently delete a task.
    
    Args:
        task_id: Primary key of task to delete.
        
    Returns:
        Redirect to index page after deletion.
    """
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/toggle/<int:task_id>")
def toggle(task_id):
    """Toggle completion status of a task.
    
    Args:
        task_id: Primary key of task to toggle.
        
    Returns:
        Redirect to index page after toggle.
    """
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/summarize", methods=["POST"])
def summarize():
    """Handle text summarization requests.
    
    Supports both form-data and JSON input.
    
    Returns:
        JSON: For API requests with summary or error
        Rendered Template: For browser submissions
        
    Raises:
        400: If no text provided
        500: If summarization fails
    """
    if request.is_json:
        text = request.json.get("text")
    else:
        text = request.form.get("text")

    if not text or not text.strip():
        return jsonify({"error": "No text provided"}), 400

    try:
        summary = get_summary(text)
        if request.is_json:
            return jsonify({"summary": summary})
        return render_template("index.html", summary=summary)
    except Exception as err:  # pylint: disable=broad-except
        return jsonify({"error": str(err)}), 500


@bp.route("/pomodoro")
def pomodoro():
    """Render the Pomodoro timer interface.
    
    Returns:
        Rendered pomodoro timer template.
    """
    return render_template("pomodoro.html")