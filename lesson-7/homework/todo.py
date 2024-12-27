import os
import json

class ToDoAPP:
    def __init__(self, task_id, title, description, date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.date = date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.date}, {self.status}"

class ToDoAppkication:
    FILENAME = 'todo.txt'
    JSONFILE = 'todo.json'

    def add_task(self):
        if not os.path.exists(self.FILENAME):
            print(f"No such file or directory: '{self.FILENAME}'")
            return
        task_id = input('Enter Task ID: ')
        if self.check_task_id_exist(task_id):
            print('This ID already exist')
            return
        title = input('Enter Title: ')
        description = input('Enter Description: ')
        date = input('Enter Due Date(YYYY-MM-DD): ')
        status = input('Enter Status (Pending/In Progress/Completed): ')

        task = ToDoAPP(task_id, title, description, date, status)
        with open(self.FILENAME, 'a') as file:
            file.write(str(task) + '\n')
            print('Task added successfully!')

    def view_all_tasks(self):
        if not os.path.exists(self.FILENAME):
            print(f"No such file or directory: '{self.FILENAME}'")
            return
        with open(self.FILENAME, 'r') as file:
            for line in file:
                print(line.strip())
    
    def update_task(self):
        if not os.path.exists(self.FILENAME):
            print(f"No such file or directory: '{self.FILENAME}'")
            return
        task_id = input('Enter task ID to update: ')
        updated_text = []
        found = False
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(task_id + ","):
                    print(f'Current record: {line.strip()}')
                    found = True
                    id = input('Enter task id: ')
                    if self.check_task_id_exist(id):
                        print('This id already exist')
                        return
                    title = input('Enter task title: ')
                    description = input('Enter task description: ')
                    date = input('Enter task date(YYYY-MM-DD): ')
                    status = input('Enter task status (Pending/In Progress/Completed): ')
                    fields = line.strip().split(", ")
                    if id:
                        fields[0] = id
                    if title:
                        fields[1] = title
                    if description:
                        fields[2] = description
                    if date:
                        fields[3] = date
                    if status:
                        fields[3] = status
                    updated_text.append(", ".join(fields) + "\n")
                else:
                    updated_text.append(line)
        if found:
            with open(self.FILENAME, "w") as file:
                file.writelines(updated_text)
            print("Task record updated.")
        else:
            print("Task not found.")
        
        
    def delete_task(self):
        if not os.path.exists(self.FILENAME):
            print(f"No such file or directory: '{self.FILENAME}'")
            return
        task_id = input('Enter task ID to delete: ')
        updated_text = []
        found = False
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(task_id + ","):
                    found = True
                else:
                    updated_text.append(line)
        if found:
            with open(self.FILENAME, "w") as file:
                file.writelines(updated_text)
            print("Task record deleted.")
        else:
            print("Task not found.")
    
    def filter_tasks(self):
        if not os.path.exists(self.FILENAME):
            print(f"No such file or directory: '{self.FILENAME}'")
            return
        task_status = input('Enter task status to filter: ')
        found = False
        with open(self.FILENAME, 'r') as file:
            for line in file:
                record = line.strip().split(', ')
                if record[4].lower() == task_status.lower():
                    found = True
                    print(line.strip())           
        if not found: print('No task found')
    
    def save_tasks(self):
        tasks_dict = {}
        cnt = 0
        titles = ['ID:', 'Title:', 'Description:', 'Date:', 'Status:']
        with open(self.FILENAME, 'r') as file:
            for row in file:
                cnt += 1
                tasks_list = row.strip().split(',')
                task_dict = {k:v for k,v in zip(titles, tasks_list)}
                tasks_dict[cnt] = task_dict

        with open(self.JSONFILE, 'w') as file:
                json.dump(tasks_dict, file, indent=4)
        print('JSON file created successfully!')
    
    def load_tasks(self):
        print('Sorry this service does not work now')
    
    def check_task_id_exist(self, task_id):
        found = False
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(task_id + ','):
                    found = True
                    return found
        if not found: return False


    def main(self):
        print('Welcome to the To-Do Application!')
        while True:
            print('\n1. Add a new task')
            print('2. View all tasks')
            print('3. Update a task')
            print('4. Delete a task')
            print('5. Filter tasks by status')
            print('6. Save tasks')
            print('7. Load tasks')
            print('8. Exit')
            choise = input('>>>>  ')

            if choise == '1':
                self.add_task()
            elif choise == '2':
                self.view_all_tasks()
            elif choise == '3':
                self.update_task()
            elif choise == '4':
                self.delete_task()
            elif choise == '5':
                self.filter_tasks()
            elif choise == '6':
                self.save_tasks()
            elif choise == '7':
                self.load_tasks()
            elif choise == '8':
                break
            else:
                print('Please enter numbers between 1 and 6')

if __name__ == '__main__':
    ToDoAppkication().main()