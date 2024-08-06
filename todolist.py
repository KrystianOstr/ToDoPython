class Task: 
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def display(self):
        print(f'Task: {self.title}, description: {self.description}.')

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def remove_task(self, title):

        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f'Task {title} removed')
                break
        else:
                print(f'Task doesn`t exists')

    def display_tasks(self):
        if len(self.tasks) > 0:
            for i, task in enumerate(self.tasks, start=1):
                print(f'Task no. {i}: ')
                task.display()
                print(f'------')
        else:
            print(f'There is no task to display.')


def main():
    task_manager = TaskManager()
    menu = ['1. Add Task', '2. Remove Task', '3. Display Tasks', '4. Exit']

    while True:
        for item in menu:
            print(f'{item}')
        user_input = int(input('\nType number to choose an option: \n'))
        print('---------')
        
        if user_input == 1:
            add_task_title_input = input('Type the title of the task: ')
            add_task_description_input = input('Type the description of the task: ')    
            task_manager.add_task(add_task_title_input, add_task_description_input)        
        elif user_input == 2:
            remove_task_title_input = input('Type the title of the task to remove: ')
            task_manager.remove_task(remove_task_title_input)
        elif user_input == 3:
            task_manager.display_tasks()
        elif user_input == 4:
            print('Goodbye!')
            break
        else:
            print('Type numbers from 1 - 4')

        print('---------')

main()