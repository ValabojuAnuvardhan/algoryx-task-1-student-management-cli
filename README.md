# Student Management CLI

A menu-driven command-line Student Management System built with Python.

## Features

- Add student
- View students
- Search students
- Update student details
- Delete students
- JSON-based persistent storage
- Input validation
- Exception handling
- Application logging

## Technologies

- Python 3
- JSON
- Python Logging

## Project Structure

```text
task-1/
│
├── main.py
├── data/
│   └── students.json
├── app.log
└── README.md

How to Run
1. Install Python 3.
2. Clone the repository.
3. Open the project directory.
4. Run:
python main.py

Data Storage
Student records are stored in:
data/students.json

The JSON file allows student information to persist after the application is closed.
Error Handling
The application handles invalid menu choices, invalid student IDs, empty input, invalid email addresses, missing data files, and invalid JSON data.

