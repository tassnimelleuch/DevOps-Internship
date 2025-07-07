from flask import Blueprint, render_template, request, jsonify
from app.services.summarizer import get_summary

bp = Blueprint('summarize', __name__)

@bp.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            summary = get_summary(text)
            return jsonify(summary=summary)
    return render_template('summarize.html')