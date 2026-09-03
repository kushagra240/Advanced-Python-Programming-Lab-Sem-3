"""Examination Hall Management System and Unique Paths dynamic programming."""


class Student:
    """Store a student's examination seating information."""

    VALID_BLOCKS = {"A", "B", "C"}

    def __init__(self, name, roll_number, hall_number, block):
        block = block.upper()
        if block not in self.VALID_BLOCKS:
            raise ValueError("Block must be A, B, or C.")

        self.name = name
        self.roll_number = roll_number
        self.hall_number = hall_number
        self.block = block

    def display_information(self):
        """Display the student's details."""
        print(
            f"Name: {self.name}, Roll Number: {self.roll_number}, "
            f"Hall Number: {self.hall_number}, Block: {self.block}"
        )

    def __str__(self):
        return (
            f"{self.roll_number} - {self.name} "
            f"(Hall {self.hall_number}, Block {self.block})"
        )


class ExamHall:
    """Maintain and display students grouped by examination block."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")
        self.students.append(student)

    def display_seating_arrangement(self):
        """Display all students under Block A, Block B, and Block C."""
        print("\nExamination Hall Seating Arrangement")
        print("=" * 40)

        for block in ("A", "B", "C"):
            print(f"\nBlock {block}")
            block_students = [student for student in self.students
                              if student.block == block]
            if not block_students:
                print("No students assigned.")
                continue

            for student in block_students:
                print(f"- {student}")


def unique_paths(rows, columns):
    """Return the number of paths from the top-left to bottom-right cell.

    A move is allowed only to the right or downward.
    """
    if rows <= 0 or columns <= 0:
        raise ValueError("Rows and columns must be positive.")

    paths = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        paths[row][0] = 1
    for column in range(columns):
        paths[0][column] = 1

    for row in range(1, rows):
        for column in range(1, columns):
            paths[row][column] = paths[row - 1][column] + paths[row][column - 1]

    return paths[rows - 1][columns - 1]


def main():
    exam_hall = ExamHall()
    exam_hall.add_student(Student("Aarav", 101, 1, "A"))
    exam_hall.add_student(Student("Meera", 102, 2, "B"))
    exam_hall.add_student(Student("Karan", 103, 1, "A"))
    exam_hall.add_student(Student("Neha", 104, 3, "C"))

    exam_hall.display_seating_arrangement()
    print(f"\nUnique paths in a 3 x 3 grid: {unique_paths(3, 3)}")


if __name__ == "__main__":
    main()
