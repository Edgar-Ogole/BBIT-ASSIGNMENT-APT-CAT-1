class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name} department.")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure: {total}")

    def display_all_employees(self):
        print(f"\nEmployees in {self.department_name} Department:")
        if not self.employees:
            print("No employees.")
        for emp in self.employees:
            emp.display_details()


# Interactive section
if __name__ == "__main__":
    department = Department("ICT Department")

    while True:
        print("\nOptions: 1) Add Employee 2) Update Salary 3) Show Employees 4) Total Salary 5) Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            eid = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            emp = Employee(name, eid, salary)
            department.add_employee(emp)

        elif choice == '2':
            eid = input("Enter employee ID to update: ")
            new_salary = float(input("Enter new salary: "))
            found = False
            for emp in department.employees:
                if emp.employee_id == eid:
                    emp.update_salary(new_salary)
                    found = True
                    break
            if not found:
                print("Employee not found.")

        elif choice == '3':
            department.display_all_employees()

        elif choice == '4':
            department.total_salary_expenditure()

        elif choice == '5':
            break
