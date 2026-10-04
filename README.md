# Student Management CLI

A menu-driven command-line Student Management System built with Python.

The application provides complete CRUD operations for student records and stores the data persistently in a JSON file.

## Features

- Add students
- View all students
- Search students by ID or name
- Update student details
- Delete students
- JSON-based persistent storage
- Automatic student ID generation
- Input validation
- Exception handling
- Case-insensitive name search
- Menu-driven command-line interface
- Modular storage management

## Technologies

- Python 3
- JSON
- Python Standard Library

## Project Structure
task-1/
│
├── main.py
├── storage.py
├── README.md
├── .gitignore
│
└── data/
    └── student.json

Requirements
- Python 3.x
- No external Python packages are required.
How to Run
1. Clone the repository
git clone <https://github.com/ValabojuAnuvardhan/algoryx-task-1-student-management-cli>

2. Open the project directory
cd task-1

3. Run the application
python main.py

Application Menu
========================================
       STUDENT MANAGEMENT SYSTEM
========================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
========================================

[# Data Storage]
Student records are stored in:
data/student.json

The application automatically loads student records when it starts and saves changes to the JSON file.
Example:
```json
[
    {
        "id": 1,
        "name": "Anu",
        "email": "anu@gmail.com",
        "course": "CSE"
    }
]

```


****CRUD Operations****
# Create
Users can add a new student by providing:
- Name
- Email
- Course
A unique student ID is generated automatically.
# Read
Users can view all stored student records.
# Update
Users can update an existing student's:
- Name
- Email
- Course
Leaving a field blank keeps its current value.
# Delete
Users can delete a student using the student's ID.
# Search
Students can be searched using:
- Student ID
- Student name
Name searches are case-insensitive.

**Input Validation**

The application validates user input including:
- Empty student names
- Empty courses
- Invalid email addresses
- Non-numeric student IDs
- Empty search values
- Invalid menu choices

**Exception Handling**

The application handles common errors including:
- Missing JSON data file
- Invalid JSON data
- Invalid numeric input
- File writing errors
- Non-existent student IDs
The application displays an appropriate message instead of terminating unexpectedly.

**Testing**

The following scenarios were tested successfully:
- Adding a student
- Viewing students
- Searching by student ID
- Searching by student name
- Case-insensitive name search
- Updating student details
- Deleting students
- Invalid email input
- Empty search input
- Invalid update ID
- Invalid delete ID
- Non-existent student ID
- Invalid menu choice
- Application exit

**Architecture**

The application separates application logic from data storage.
main.py
   │
   ├── Add Student
   ├── View Students
   ├── Search Student
   ├── Update Student
   ├── Delete Student
   └── Menu Management
          │
          ▼
     storage.py
          │
          ├── load_students()
          └── save_students()
          │
          ▼
   data/student.json

This separation keeps the application code organized and makes the storage functionality reusable.

**Learning Outcomes**

This project demonstrates practical understanding of:
- Python programming
- Command-line application development
- CRUD operations
- JSON persistence
- Input validation
- Exception handling
- Modular programming
- File handling
- Git and GitHub
- Software engineering practices
Author
## Valaboju Anuvardhan Chary