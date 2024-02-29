import json

class EmployeeSystem:
    def __init__(self):
        self.employees = []

    def load_employees_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.employees = json.load(file)
        except FileNotFoundError:
            print("Файл не найден. Создан новый список сотрудников")

    def save_employees_to_file(self, file_name):
        with open(file_name, "w") as file:
            json.dump(self.employees, file, indent=4)

    def add_employee(self, employee_data):
        self.employees.append(employee_data)

    def edit_employee(self, employee_index, new_employee_data):
        self.employees[employee_index] = new_employee_data

    def delete_employee(self, employee_index):
        del self.employees[employee_index]

    def find_employee_by_lastname(self, last_name):
        found_employees = [employee for employee in self.employees if employee.get('last_name') == last_name]
        return found_employees

    def find_employees_by_age(self, age):
        found_employees = [employee for employee in self.employees if employee.get('age') == age]
        return found_employees

    def find_employees_by_lastname_initial(self, initial):
        found_employees = [employee for employee in self.employees if employee.get('last_name').startswitch(initial)]
        return found_employees


employee_system = EmployeeSystem()
employee_system.load_employees_from_file("employees.json")

employee_data = {
    "first_name": "Иван",
    "last_name": "Иванов",
    "age": 30,
    "position": "Программист"
}

employee_system.add_employee(employee_data)

employee_system.edit_employee(0, {"first_name": "Петр", "last_name": "Петров", "age": 35, "position": "Аналитик"})
employee_system.delete_employee(0)

found_by_lastname = employee_system.find_employee_by_lastname("Иванов")
found_by_age = employee_system.find_employees_by_age(30)
found_by_initial = employee_system.find_employees_by_lastname_initial("И")

employee_system.save_employees_to_file("employees.json")

