# TaskNest - To Do List Web Application
This is a simple To-Do List web application built using Flask and SQLAlchemy. It supports all CRUD operations (Create, Read, Update, Delete) allowing users to manage tasks effectively.

## Features
1. <b>View Tasks</b>: See a list of tasks with their creation dates.
2. <b>Add Task</b>: Add new tasks to the list.
3. <b>Update Task</b>: Modify existing tasks.
4. <b>Delete Task</b>: Remove tasks from the list.
   
## Technologies Used
1. Python
2. Flask
3. SQLAlchemy
4. HTML/CSS (for front-end)
   
## Setup Instructions

### Prerequisites
1. Python 3.x installed on your system.
2. pip package manager.
3. SQLite database.
   
### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/kshitij7704/To_Do_List_Flask_App.git
cd To_Do_List_Flask_App
```
2. Set up virtual environment:
```bash
python -m venv venv
# On Mac use
source venv/bin/activate
# On Windows use
venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Initialize the database:
```bash
python create_db.py
```
This will create a SQLite database (list.db) in the instance directory and set up necessary tables.

5. Run the application:
```bash
python app.py
```
Open your web browser and go to http://localhost:5000 to view the application.

## Usage
1. <b>Adding a Task</b>: Enter a task in the input field and click "Add Task".
2. <b>Updating a Task</b>: Click "Update" next to the task you want to modify, make changes in the form, and click "Update Task".
3. <b>Deleting a Task</b>: Click "Delete" next to the task you want to remove from the list.

