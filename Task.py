#this is a function to create task
def create_task(task):
    try:
        task_file = open("task.txt", "a")
        task_file.write(task+'\n')
        task_file.close()
        return("Task created")
    except:
        return("File not found")
        
# this is a function to read the tasks and return task list
def read_tasks():
    try:
        task_file = open("task.txt", "r")
        tasks = task_file.readlines()
        return tasks
    except:
        return("File/Tasks not found")

#this is a function to delete task
def delete_task(task_to_delete):
    try:
        tasks = read_tasks()
        new_task_file = open("task.txt", "w")
        for task in tasks:
            if task.strip("\n") != task_to_delete:
                new_task_file.write(task)
    except:
        print("File/Tasks not found")
