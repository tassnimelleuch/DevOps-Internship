"""Text summarization routes."""
import logging
from flask import Blueprint, render_template, request, jsonify
from app.services.summarizer import get_summary
bp = Blueprint('summarize', __name__)
logger = logging.getLogger(__name__)
@bp.route('/summarize', methods=['GET', 'POST'])
def summarize():
    """handle text summarization requests."""
    if request.method == 'POST':
        try:
            # Get input (both JSON and form data)
            text = request.json.get('text', '').strip() if request.is_json else request.form.get('text', '').strip()
            if not text:
                return jsonify(error="Text required"), 400
                        # THE CRITICAL PART - must let exceptions propagate
            summary = get_summary(text)  # This MUST be allowed to raise exceptions
            return jsonify(summary=summary), 200
        except Exception :  # pylint: disable=broad-exception-caught
            return jsonify(error="Summarization failed"), 500
    return render_template('summarize.html')
