from functions import get_todos, add_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, edit, completed, show or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        add_todo(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, x in enumerate(todos):
            x = x.strip('\n')
            print (f"{index + 1} -{x} ")

    elif  user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("enter new todo")
            todos[number -1] = new_todo + '\n'

            add_todo(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("completed"):
        try:
            number = int(user_action[10:])

            todos =  get_todos()
            todo_to_remove = todos[number -1].strip('\n')
            todos.pop(number -1)

            add_todo(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
        except IndexError:
            print("Your number does not exist")
            continue
    elif user_action.startswith("exit"):
        break

    else: print("Command is not valid")

print("Bye!")

