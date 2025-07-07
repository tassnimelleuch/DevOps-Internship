# TaskFlow: To-Do List, Summarizer, and Pomodoro Timer

TaskFlow is a modern productivity web app built with Flask. It helps you manage your tasks, summarize long texts using AI, and stay focused with a Pomodoro timer—all in a beautiful, easy-to-use interface.

---

## ✨ Features
- **To-Do List:** Add, edit, complete, and delete your daily tasks.
- **Text Summarizer:** Summarize any text using the BART large CNN model from Hugging Face.
- **Pomodoro Timer:** Stay productive with a built-in Pomodoro timer (25 min work / 5 min break), including a floating timer widget and alarm sound.

---

## 🚀 Quick Start

### 1. Clone the Repository


### 2. Install Python Requirements
Make sure you have Python 3.8+ and pip installed.

```bash
pip install -r app/requirements.txt
```

**Required packages:**
- Flask
- SQLAlchemy
- transformers
- torch
- sentencepiece

### 3. Add an Alarm Sound (for Pomodoro)
Place a short sound file (e.g., `alarm.mp3`) in the `app/static/` directory. You can use any `.mp3` file you like.

### 4. Run the App
```bash
python run.py
```


### 5. Open in Your Browser
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🤖 How the Summarizer Works
- The first time you use the summarizer, the app will automatically download the `facebook/bart-large-cnn` model from Hugging Face (~1.5GB). This requires an internet connection.
- The model is cached for future use (no repeated downloads).
- No model files are stored in this repo.

---

# Hugging Face cache
.cache/huggingface/
models/
```



