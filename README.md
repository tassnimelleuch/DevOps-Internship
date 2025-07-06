# Flask Todo Application

A modular Flask application for managing todo tasks.

## Project Structure

```
DevOps-Internship/
├── app/
│   ├── __init__.py          # Application factory
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models
│   ├── routes.py           # Route handlers
│   ├── config.py           # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       └── edit.html
├── run.py                  # Alternative entry point
└── README.md
```

## Features

- Add, edit, delete, and toggle todo tasks
- SQLite database for data persistence
- Modular architecture suitable for SonarQube analysis
- Application factory pattern for better testing and deployment

## Installation

1. Install dependencies:
```bash
pip install -r app/requirements.txt
```

## Running the Application

### Option 1: From the app directory
```bash
cd app
python app.py
```

### Option 2: From the root directory
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Modular Structure Benefits

This application has been refactored into modules for better:

- **Maintainability**: Each component has a single responsibility
- **Testability**: Individual modules can be tested in isolation
- **SonarQube Analysis**: Modular structure allows for better code quality analysis
- **Scalability**: Easy to add new features without affecting existing code

## Modules

- **models.py**: Contains the Task database model
- **routes.py**: Contains all route handlers and business logic
- **config.py**: Configuration settings for different environments
- **__init__.py**: Application factory for creating Flask instances
