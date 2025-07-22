"""Text summarization routes and handlers."""

from flask import Blueprint, jsonify, render_template, request

from app.services.summarizer import get_summary

bp = Blueprint("summarize", __name__)


@bp.route("/summarize", methods=["GET", "POST"])
def summarize():
    """Handle text summarization requests.

    GET: Render the summarization form
    POST: Process text and return summary

    Returns:
        Response: Either HTML form or JSON summary
    """
    if request.method == "POST":
        text = request.form.get("text")
        if not text or not text.strip():
            return jsonify(error="No text provided"), 400

        try:
            summary = get_summary(text)
            return jsonify(summary=summary)
        except Exception as e:  # pylint: disable=broad-except
            return jsonify(error=str(e)), 500

    return render_template("summarize.html")
