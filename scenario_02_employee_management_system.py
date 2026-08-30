class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def get_salary_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        return "Low Salary"

    def __str__(self):
        return (
            f"Employee ID: {self.employee_id}, "
            f"Name: {self.name}, "
            f"Salary: ₹{self.salary}, "
            f"Category: {self.get_salary_category()}"
        )


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print(f"\nEmployees at {self.name}:\n")
        if not self.employees:
            print("No employees added yet.")
            return
        for employee in self.employees:
            print(employee)


def main():
    company = Company("Skyline Tech")

    company.add_employee(Employee(1, "Rohit", 95000))
    company.add_employee(Employee(2, "Priya", 52000))
    company.add_employee(Employee(3, "Ankit", 36000))
    company.add_employee(Employee(4, "Sana", 70000))

    company.display_employees()


if __name__ == "__main__":
    main()
