import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Finding the directory for sqllte database
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'list.db')

if not os.path.exists(os.path.join(basedir, 'instance')):
    os.makedirs(os.path.join(basedir, 'instance'))


# Configuring the sqlite database URI and disable sqlalchemy modification tracking
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Defining the ToDo model for the database
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


# Route for the main page
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # For new task submission
        task_content = request.form['content']
        if not task_content.strip():
            return "The task content cannot be empty."

        new_task = ToDo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There was an issue adding your task: {e}"

    else:
        # Retrieval and display all tasks
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        return render_template("index.html", tasks=tasks)


# Route for deleting a task
@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = ToDo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting the task"


# Route for updating a task
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    task= ToDo.query.get_or_404(id)
    if request.method == 'POST':
        # Update the task
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task"

    else:
        # Display the update task page
        return render_template("update.html", task=task)


# Main function for running the flask app
if __name__ == "__main__":
    app.run(debug=True)