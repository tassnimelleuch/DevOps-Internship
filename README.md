# TaskFlow: To-Do List, Summarizer, and Pomodoro Timer

TaskFlow is a modern productivity web app built with Flask. It helps you manage your tasks, summarize long texts using AI, and stay focused with a Pomodoro timer—all in a beautiful, easy-to-use interface.

---

## ✨ Features
- To-Do List: Add, edit, complete, and delete your daily tasks.
- Text Summarizer: Summarize any text using the BART large CNN model from Hugging Face.
- Pomodoro Timer: Stay productive with a built-in Pomodoro timer (25 min work / 5 min break), including a floating timer widget and alarm sound.

---

## 🚀 Quick Start (Python)

1. Clone the Repository
2. Install Python Requirements
   - Make sure you have Python 3.8+ and pip installed.
   - Install dependencies:
     pip install -r app/requirements.txt

3. Start the Flask Application
   python run.py
   - The application will automatically initialize the database on first run
   - Open in your browser at http://127.0.0.1:5000

---

## 🐳 Quick Start with Docker

1. Build the Docker Image
   docker build -t taskflow-app .

2. Run the Docker Container
   docker run -p 5000:5000 taskflow-app

3. Open in Your Browser
   - Go to http://localhost:5000

4. Stop the App
   - Press Ctrl+C in the terminal, or run:
     docker ps
     docker stop <CONTAINER_ID>

---

## 📊 Code Quality Report
This project is analyzed by SonarCloud for bugs, vulnerabilities, and code smells. Go to https://sonarcloud.io/project/overview?id=tassnimelleuch_DevOps-Internship

---

## 🤖 How the Summarizer Works
- The first time you use the summarizer, the app will automatically download the facebook/bart-large-cnn model from Hugging Face (~1.5GB). This requires an internet connection.
- The model is cached for future use (no repeated downloads).
- No model files are stored in this repo.

---

## 🛠️ Troubleshooting
- If you get a port error, make sure nothing else is using port 5000.
- If you change the code, rebuild the Docker image before running again.
- For any issues, check the logs in your terminal for error messages.

---

## 🔧 Automated CI/CD Pipeline
This project includes a complete CI/CD pipeline that automatically:
- Runs pylint for code quality analysis
- Executes SonarQube scanning for comprehensive code inspection
- Runs unit tests to ensure functionality
- Builds Docker images on successful tests
- Pushes images to DockerHub
- Deploys to Azure cloud platform

---

Happy productivity! 🎉