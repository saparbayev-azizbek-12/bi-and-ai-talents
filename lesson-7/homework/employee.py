class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILENAME = 'employee.txt'

    def check_employee_exist(self, emp_id):
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(emp_id + ','):
                    return True
                return False

    def add_employee(self):
        emp_id = input('Enter employee ID to add: ')
        if self.check_employee_exist(emp_id):
            print('This ID already exist')
            return
        name = input('Enter employee name: ')
        position = input('Enter employee position: ')
        salary = input('Enter employee salary: ')
        employee = Employee(emp_id, name, position, salary)
        with open(self.FILENAME, 'a') as file:
            file.write(str(employee) + '\n')
        print('Employee added successfully!')

    def view_all_employees(self):
        with open(self.FILENAME, 'r') as file:
            for line in file:
                print(line.strip())

    def search_employees(self):
        emp_id = input('Enter employee ID to search: ')
        found = False
        employee = ''
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(emp_id + ','):
                    found = True
                    employee = line            
        if found: print(employee)
        else: print('No employee found')
        
    def update_employees(self):
        emp_id = input('Enter employee ID to update: ')
        updated_text = []
        found = False
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print(f'Current record: {line.strip()}')
                    found = True
                    name = input('Enter employee name: ')
                    position = input('Enter employee position: ')
                    salary = input('Enter employee salary: ')
                    fields = line.strip().split(", ")
                    if name:
                        fields[1] = name
                    if position:
                        fields[2] = position
                    if salary:
                        fields[3] = salary
                    updated_text.append(", ".join(fields) + "\n")
                else:
                    updated_text.append(line)
        if found:
            with open(self.FILENAME, "w") as file:
                file.writelines(updated_text)
            print("Employee record updated.")
        else:
            print("Employee not found.")
            
    def delete_employees(self):
        emp_id = input("Enter Employee ID to delete: ")
        updated_records = []
        found = False
        with open(self.FILENAME, "r") as file:
            for record in file:
                if record.startswith(emp_id + ","):
                    found = True
                else:
                    updated_records.append(record)
        if found:
            with open(self.FILENAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted.")
        else:
            print("Employee not found.")


    def main(self):
        while True:
            print('1. Add new employee record')
            print('2. View all employee records')
            print('3. Search for an employee by Employee ID')
            print('4. Update an employee\'s information')
            print('5. Delete an employee record')
            print('6. Exit')
            choise = input('>>>>  ')

            if choise == '1':
                self.add_employee()
            elif choise == '2':
                self.view_all_employees()
            elif choise == '3':
                self.search_employees()
            elif choise == '4':
                self.update_employees()
            elif choise == '5':
                self.delete_employees()
            elif choise == '6':
                break
            else:
                print('Please enter numbers between 1 and 6')

if __name__ == '__main__':
    EmployeeManager().main()