class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        return "F"

    def __str__(self):
        return (
            f"Roll Number: {self.roll_number}, "
            f"Name: {self.name}, "
            f"Marks: {self.marks}, "
            f"Grade: {self.get_grade()}"
        )


class College:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"\nStudents in {self.name}:\n")
        if not self.students:
            print("No students added yet.")
            return
        for student in self.students:
            print(student)


def main():
    college = College("Green Valley College")

    college.add_student(Student(101, "Aarav", 96))
    college.add_student(Student(102, "Meera", 82))
    college.add_student(Student(103, "Karan", 68))
    college.add_student(Student(104, "Neha", 54))

    college.display_students()


if __name__ == "__main__":
    main()
