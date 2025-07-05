from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'instance', 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content']
    new_task = Task(content=task_content)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    task = Task.query.get_or_404(id)
    return render_template('edit.html', task=task)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    task = Task.query.get_or_404(id)
    task.content = request.form['content']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle(id):
    task = Task.query.get_or_404(id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)