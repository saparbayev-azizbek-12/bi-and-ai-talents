import csv
import json

class Task:
    def __init__(self, id, task, completed, priority):
        self.id = id
        self.task = task
        self.completed = completed
        self.priority = priority

    def __str__(self):
        return f"{self.id}, {self.task}, {self.completed}, {self.priority}"
    
class ManageTasks:
    pass

class ConsoleAPP:
    def run(self):
        self.menu()

    def menu(self):
        while True:
            print("1.Add task")
            print("2.Display all tasks")
            print("3.Display task completion stats")
            print("4.Update task")

if __name__ == '__main__':
    app = ConsoleAPP()
    app.run()