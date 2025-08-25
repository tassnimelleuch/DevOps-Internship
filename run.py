"""Main application entry point for the Flask Todo App."""
import os
from app import create_app, db
from app.models import Task

app = create_app()

if __name__ == '__main__':
    # Create DB tables before starting the app
    with app.app_context():
        db.create_all()
        print("✅ Database tables ensured before app start")

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
