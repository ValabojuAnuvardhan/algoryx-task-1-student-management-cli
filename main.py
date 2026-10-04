from storage import load_students, save_students


def add_student():
    print("adding student...")

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    email = input("Enter student email: ").strip()

    if "@" not in email or "." not in email:
        print("Invalid email address.")
        return

    course = input("Enter student course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    students = load_students()

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
    save_students(students)

    print(f"Student added successfully with ID: {new_id}")


def view_students():
    print("viewing students...")

    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n" + "=" * 60)
    print("                    STUDENT LIST")
    print("=" * 60)

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Email: {student['email']} | "
            f"Course: {student['course']}"
        )

    print("=" * 60)


def search_student():
    print("searching student...")

    student_details = input(
        "Enter student ID or name to search: "
    ).strip().lower()

    if not student_details:
        print("Search value cannot be empty.")
        return

    students = load_students()

    for student in students:
        if (
            str(student["id"]) == student_details
            or student["name"].lower() == student_details
        ):
            print("\nStudent found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")
            return

    print("Student not found.")


def update_student():
    print("updating student...")

    try:
        student_id = int(input("Enter student ID to update: "))

    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    students = load_students()

    for student in students:

        if student["id"] == student_id:

            print("\nCurrent details:")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")

            name = input(
                "Enter new name (leave blank to keep current): "
            ).strip()

            email = input(
                "Enter new email (leave blank to keep current): "
            ).strip()

            course = input(
                "Enter new course (leave blank to keep current): "
            ).strip()

            if name:
                student["name"] = name

            if email:
                if "@" not in email or "." not in email:
                    print("Invalid email address.")
                    return

                student["email"] = email

            if course:
                student["course"] = course

            save_students(students)

            print("Student details updated successfully.")
            return

    print("Student not found.")


def delete_student():
    print("deleting student...")

    try:
        student_id = int(input("Enter student ID to delete: "))

    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    students = load_students()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)
            save_students(students)

            print("Student deleted successfully.")
            return

    print("Student not found.")


def show_menu():
    """Display the main menu."""

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
    """Run the Student Management System."""

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

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