import os

FILE_NAME = "employees.txt"

def menu():
    print("\nEmployee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by ID")
    print("4. Update employee information")
    print("5. Delete an employee record")
    print("6. Exit")
    return input("Choose an option: ")

def add_employee():
    with open(FILE_NAME, "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added.")

def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.")
        else:
            for record in records:
                print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(FILE_NAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print(record.strip())
                found = True
                break
    if not found:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    with open(FILE_NAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                found = True
                print(f"Current record: {record.strip()}")
                name = input("Enter new Name (leave blank to keep current): ")
                position = input("Enter new Position (leave blank to keep current): ")
                salary = input("Enter new Salary (leave blank to keep current): ")
                fields = record.strip().split(", ")
                if name:
                    fields[1] = name
                if position:
                    fields[2] = position
                if salary:
                    fields[3] = salary
                updated_records.append(", ".join(fields) + "\n")
            else:
                updated_records.append(record)
    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Employee record updated.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    with open(FILE_NAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                found = True
            else:
                updated_records.append(record)
    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted.")
    else:
        print("Employee not found.")

def main():
    while True:
        choice = menu()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
