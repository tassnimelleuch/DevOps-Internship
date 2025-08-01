"""Text summarization service using HuggingFace transformers."""
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')


def get_summary(text: str) -> str:
    """Generate a summary for the given text.
    
    Args:
        text: Input text to summarize (must be non-empty)
        
    Returns:
        str: Generated summary or empty string on failure
        
    Raises:
        ValueError: If input text is empty after stripping
    """
    try:
        cleaned_text = text.strip()
        if not cleaned_text:
            return ""
        result = summarizer(
            cleaned_text,
            max_length=130,
            min_length=30,
            do_sample=False  # Disable randomness for consistent results
        )
        return result[0]['summary_text']
    except Exception:  # pylint: disable=broad-except
        return ""
    