# python
# `lecture_3/student_grade_analyzer.py`
# Student Grade Analyzer

students = []  # List of dicts: {"name": str, "grades": [int, int, ...]}


def add_student(prompt: str = "Enter student name: ") -> None:
    """
    Prompt for and add a new student to the global `students` list.
    Valid names may include letters, spaces, hyphens, and apostrophes.
    """
    allowed_chars = set(" -'")  # space, hyphen, apostrophe

    while True:
        try:
            name = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            return  # implicit None

        # Empty name is not allowed
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        # Duplicate check (case-insensitive)
        if any(student["name"].lower() == name.lower() for student in students):
            print("Student already exists.")
            continue

        # Name must not contain digits
        if any(char.isdigit() for char in name):
            print("Name cannot contain numbers. Please try again.")
            continue

        # Name must only contain letters or allowed punctuation
        if any(char not in allowed_chars and not char.isalpha() for char in name):
            print("Name contains invalid characters. Use letters, spaces, hyphens or apostrophes. Please try again.")
            continue

        # All checks passed: add student
        students.append({'name': name, 'grades': []})
        print(f"Student {name} added.")
        return  # implicit None


def add_grades(prompt_name: str = "Enter student name: ",
               prompt_grade: str = "Enter a grade (or 'done' to finish): ") -> None:
    """
    Prompt for a student name and add grades interactively.
    Grades must be integers between 0 and 100. Use 'done' to finish.
    """
    name = input(prompt_name).strip()

    for s in students:
        if s["name"].lower() == name.lower():
            # Found the student; prompt repeatedly for grades
            while True:
                grade = input(prompt_grade).strip()
                if grade.lower() == "done":
                    break
                try:
                    value = int(grade)
                    if 0 <= value <= 100:
                        s["grades"].append(value)
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return
    print("Student not found.")


def calculate_average(grades) -> float | None:
    """
    Return the average of `grades`, or None if the list is empty.
    """
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return None


def show_report() -> None:
    """
    Print a report for each student (average or N/A) and a summary (max, min, overall average).
    """
    if not students:
        print("No students to report.")
        return

    print("\n--- Student Report ---")
    averages = []

    for s in students:
        avg = calculate_average(s["grades"])
        if avg is None:
            print(f"{s['name']}'s average grade is N/A.")
        else:
            print(f"{s['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)

    print("-" * 30)

    if averages:
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages) / len(averages):.1f}")
    else:
        print("No grades available to calculate summary.")


def find_top_student() -> None:
    """
    Find and print the student with the highest average.
    """
    # Build list of (student, average) for students that have at least one grade
    valid_students = [
        (s, calculate_average(s["grades"]))
        for s in students
        if calculate_average(s["grades"]) is not None
    ]

    if not valid_students:
        print("No students with valid grades.")
        return

    top_student, top_average = max(valid_students, key=lambda x: x[1])
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_average:.1f}.")


def student_grade_analyzer() -> None:
    """
    Main interactive loop for the Student Grade Analyzer
    """
    while True:
        print(
            f"--- Student Grade Analyzer ---\n"
            f"1. Add a new student\n"
            f"2. Add a grades for a student\n"
            f"3. Generate a full report\n"
            f"4. Find the top student\n"
            f"5. Exit program"
        )

        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grades()
        elif choice == 3:
            show_report()
        elif choice == 4:
            find_top_student()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    student_grade_analyzer()
