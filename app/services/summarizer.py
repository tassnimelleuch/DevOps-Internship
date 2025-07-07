from transformers import pipeline

def get_summary(text):
    summarizer = pipeline("summarization", model="./bart-large-cnn")
    return summarizer(text, max_length=130, min_length=30)[0]['summary_text']