import json

file_path = "data/student.json"


def load_students():

    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Data file contains invalid JSON.")
        return []


def save_students(students):

    try:
        with open(file_path, "w") as file:
            json.dump(students, file, indent=4)

    except OSError as error:
        print(f"Error saving student data: {error}")