from Task import create_task, read_tasks, delete_task

# Working with tasks
def create():
    task = input('enter task ')
    create_task(task)

def read():
    tasks = read_tasks()
    print(tasks)
    # for task in tasks:

def remove(task):
    delete_task(task)

def main():
    print('Welcome to task engine ')
    tasks = list(read_tasks())
    if len(tasks) < 1:
        user = input("Seems this is your first run. Please add a new task :) :")
        create_task(user)
    user = input('What do you want to do? Create New Task(create)\nRead Tasks(read)\nDelete Task(delete)\n: ').lower()
    if user == 'create':
        create()
    elif user == 'read':
        read()
    elif user == 'delete':
        read()
        task_del = input('Please input the task to be deleted: ')
        remove(task_del)
    else:
        print('No command received')


while True:
    main()