"""Text summarization routes."""
from flask import Blueprint, render_template, request, jsonify
from app.services.summarizer import get_summary

bp = Blueprint('summarize', __name__)


@bp.route('/summarize', methods=['GET', 'POST'])
def summarize():
    """Handle summarization requests.
    
    GET: Show summarization form
    POST: Return JSON summary
    
    Returns:
        GET: Rendered HTML form
        POST: JSON with summary or error
    """
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        if not text:
            return jsonify(error="Text input is required"), 400
        summary = get_summary(text)
        return jsonify(summary=summary)
    return render_template('summarize.html')
