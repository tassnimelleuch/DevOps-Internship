# TaskFlow: To-Do App with Text Summarizer

TaskFlow is a modern Flask web application that helps you manage your tasks and also provides a powerful text summarization feature using a state-of-the-art AI model.

## Features
- 📝 **To-Do List:** Add, edit, complete, and delete your daily tasks with a beautiful, responsive interface.
- ✂️ **Text Summarizer:** Summarize any text using the BART large CNN model from Hugging Face. Great for condensing articles, notes, or any long text!

---

## Requirements
- Python 3.8+
- pip

### Python Packages
- Flask
- SQLAlchemy
- transformers
- torch
- sentencepiece

You can install all requirements with:
```bash
pip install -r app/requirements.txt
```

---

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd DevOps-Internship
   ```

2. **Install dependencies:**
   ```bash
   pip install -r app/requirements.txt
   ```

3. **Run the app:**
   ```bash
   python run.py
   ```
   or (if using Flask CLI):
   ```bash
   export FLASK_APP=app
   flask run
   ```

4. **Open your browser:**
   Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## How the Summarizer Works
- The first time you use the summarizer, the app will automatically download the `facebook/bart-large-cnn` model from Hugging Face (~1.5GB). This requires an internet connection.
- The model is cached for future use (no repeated downloads).
- You can summarize any text by clicking the **Summarize** button on the main page, entering your text, and clicking **Summarize**.

---

## Notes
- **No model files are stored in this repo.** The summarizer uses Hugging Face's model hub for easy, legal, and scalable model access.
- If you want to pre-download the model (optional):
  ```bash
  python -c "from transformers import pipeline; pipeline('summarization', model='facebook/bart-large-cnn')"
  ```
- Add these lines to your `.gitignore` to avoid committing model files:
  ```
  # Hugging Face cache
  .cache/huggingface/
  models/
  ```

---

## Screenshots
*(Add screenshots of your app here!)*

---

## License
MIT (or your preferred license)

