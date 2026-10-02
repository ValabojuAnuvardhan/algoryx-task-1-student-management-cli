import json
file_path = "data/student.json"

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    email = input("Enter student email: ").strip()

    if "@gmail.com" not in email:
        print("Invalid email address.")
        return

    course = input("Enter student course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    try:
        with open(file_path, "r") as file:
            students = json.load(file)

        if students:
            new_id = max(student["id"] for student in students) + 1
        else:
            new_id = 1

        student = {
            "id": new_id,
            "name": name,
            "email": email,
            "course": course
        }

        students.append(student)

        with open(file_path, "w") as file:
            json.dump(students, file, indent=4)

        print(f"Student added successfully with ID: {new_id}")

    except FileNotFoundError:
        print("Data file not found.")

    except json.JSONDecodeError:
        print("Data file contains invalid JSON.")

    except Exception as e:
        print(f"Unexpected error: {e}")

def view_students():
    with open(file_path,"r") as file:
        students = json.load(file) 
    if not students:
        print("No students found.")
        return
    print("....students list....")
    for student in  students:
        print(f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}, Course: {student['course']}")

def search_student():
    student_details = input("Enter student ID or name to search: ").strip().lower()
    with open(file_path, "r") as file:
        students = json.load(file)

    for student in students:
        if str(student["id"]) == student_details or student["name"].lower() == student_details:
            print("Student found:")
            print(f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}, Course: {student['course']}")
            return

    print("Student not found.")


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    with open(file_path, "r") as file:
        students = json.load(file)

    for student in students:
        if student["id"] == student_id:
            print(f"Current details: Name: {student['name']}, Email: {student['email']}, Course: {student['course']}")
            name = input("Enter new name (leave blank to keep current): ").strip()
            email = input("Enter new email (leave blank to keep current): ").strip()
            course = input("Enter new course (leave blank to keep current): ").strip()

            if name:
                student["name"] = name  
            if email:
                if "@" not in email or "." not in email:
                    print("Invalid email address.")
                    return
                student["email"] = email
            if course:
                student["course"] = course

            with open(file_path, "w") as file:
                json.dump(students, file, indent=4)
            print("Student details updated successfully.")
            return

    print("Student not found.")

def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    with open(file_path, "r") as file:
        students = json.load(file)

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            with open(file_path, "w") as file:
                json.dump(students, file, indent=4)

            print("Student deleted successfully.")
            return

    print("Student not found.")

def show_menu():
    print("\n" + "=" * 40)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 40)


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ",)

        if choice == "1":
            add_student()


        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
