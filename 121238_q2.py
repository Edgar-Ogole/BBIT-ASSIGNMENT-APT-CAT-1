class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade}.")

    def display_grades(self):
        print(f"\nGrades for {self.name}:")
        if not self.assignments:
            print("No assignments found.")
        else:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.course_name}.")

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)
                return
        print("Student not found.")

    def display_all_grades(self):
        print(f"\nGrades for course: {self.course_name}")
        if not self.students:
            print("No students enrolled.")
        for student in self.students:
            print(f"\nStudent: {student.name} ({student.student_id})")
            student.display_grades()


# Interactive section
if __name__ == "__main__":
    instructor = Instructor("Dr. Jane", "Web Development")

    while True:
        print("\nOptions: 1) Add Student 2) Assign Grade 3) Show All Grades 4) Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            sid = input("Enter student ID: ")
            student = Student(name, sid)
            instructor.add_student(student)

        elif choice == '2':
            sid = input("Enter student ID: ")
            assignment = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(sid, assignment, grade)

        elif choice == '3':
            instructor.display_all_grades()

        elif choice == '4':
            break
