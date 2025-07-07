from transformers import pipeline

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

def get_summary(text: str) -> str:
    result = summarizer(text, max_length=130, min_length=30)
    return result[0]['summary_text']  # type: ignore