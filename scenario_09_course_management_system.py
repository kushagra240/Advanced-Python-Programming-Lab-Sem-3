class Course:
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    def get_category(self):
        if self.duration >= 6:
            return "Long-Term"
        return "Short-Term"

    def __str__(self):
        return (
            f"Course Name: {self.course_name}, "
            f"Duration: {self.duration} months, "
            f"Fee: ₹{self.fee}, "
            f"Category: {self.get_category()}"
        )


class Institute:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"\nCourses offered by {self.name}:\n")
        if not self.courses:
            print("No courses available.")
            return
        for course in self.courses:
            print(course)


def main():
    institute = Institute("Future Skills Institute")

    institute.add_course(Course("Python Programming", 3, 15000))
    institute.add_course(Course("Data Science", 6, 32000))
    institute.add_course(Course("Web Development", 4, 22000))
    institute.add_course(Course("Machine Learning", 8, 45000))

    institute.display_courses()


if __name__ == "__main__":
    main()
