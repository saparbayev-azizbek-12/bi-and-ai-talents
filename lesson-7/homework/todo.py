class ToDoAppkication:
    FILENAME = 'todo.txt'

    def add_task(self):
        task_id = input('Enter Task ID: ')
        title = input('Enter Title: ')
        description = input('Enter Description: ')
        date = input('Enter Due Date(YYYY-MM-DD): ')
        status = input('Enter Status (Pending/In Progress/Completed): ')

    def view_all_tasks(self):
        pass
    
    def update_task(self):
        pass
    
    def delete_task(self):
        pass
    
    def filter_tasks(self):
        pass
    
    def save_tasks(self):
        pass
    
    def load_tasks(self):
        pass
    
    def check_task_id_exist(self, task_id):
        with open(self.FILENAME, 'r') as file:
            for line in file:
                if line.startswith(task_id + ','):
                    return True
                return False

    def main(self):
        print('Welcome to the To-Do Application!')
        while True:
            print('1. Add a new task')
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