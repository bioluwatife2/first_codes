# this function is to create a todo list
def create_todo(todo):
    try:
        todo_list = open("todo.txt","a")
        todo_list.write(todo+'\n')
        todo_list.close()
        print("Todo created")
    except:
        print("File not found")

# this function is to read the todo and return todo list\
def read_todos():
    try:
        todo_list = open("todo.txt","r")
        todos = todo_list.readlines()
        return todos
    except:
        print("file/task not found")

#this is a function to delete todo list
def delete_todo(todo_to_delete):
    try:
        todos = read_todos()
        new_todo_list = open("todo.txt","w")
        for todo in todos:
            if todo.strip("\n")!= todo_to_delete:
                new_todo_list.write(todo)
    except:
        print("file not found")