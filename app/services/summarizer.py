"""Text summarization service using Hugging Face transformers."""

from transformers import pipeline

# Initialize the summarization pipeline at module level (avoids repeated
# loading)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def get_summary(text: str) -> str:
    """Generate a summary of the input text using BART model.

    Args:
        text: Input text to be summarized.

    Returns:
        str: Generated summary text.

    Raises:
        ValueError: If input text is empty or too short.
        RuntimeError: If summarization fails.
    """
    if not text or len(text.strip()) < 30:
        raise ValueError("Input text must be at least 30 characters")

    try:
        result = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return str(result[0]["summary_text"])
    except Exception as err:
        raise RuntimeError(f"Summarization failed: {err}") from err
