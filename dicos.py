todos ={}

while True:
    newTodo = input("New Todo: ")
    if newTodo == "":
        break

    if newTodo in todos:
        print("Todo: "+newTodo+" exists.")
    else:
        todoDetails = input("Details: ")
        todos[newTodo] = todoDetails
        print(newTodo+" added")



