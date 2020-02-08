from ToDo_List import create_todo, read_todos, delete_todo
def create():
    todo = input("Enter Todo: ")
    create_todo(todo)

def read():
    todos = read_todos()
    print(todos)

def remove(todo):
    delete_todo(todo)

def main():
    print("Welcme to Todo...")
    todos = list(read_todos())
    if len(todos) < 1:
        user = input("oops! seems this looks ikr your first time. Kindly enter a new list")
        create_todo(user)
    user = input("What do you want to do? Create New todo(create)\nRead todos(read)\nDelete todos(delete)\n: ").lower()
    if user == 'create':
        create()
    elif user == 'read':
        read()
    elif user == 'delete':
        read()
        todo_del = input('Please input the todo to be deleted: ')
        remove(todo_del)
    else:
        print('No command received')


while True:
    main()