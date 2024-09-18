
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        todos_local = remove_empty_lines(todos_local)
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

def remove_empty_lines(todos_list):
    todoss=[]
    for todo in todos_list:
        if todo != "\n":
            todoss.append(todo)
    todos_list = todoss
    return todos_list

def move_in_list_up(enumerated_todoes):
    pass


def enumerate_todo_list():
    enumerated_todos = []
    todoes = get_todos(filepath=FILEPATH)
    for first_char in todoes:
        if first_char[0] != 1:
            enumerated_todoes = [f"{index + 1}. {todo}" for index, todo in enumerate(todoes)]
            for todo in enumerated_todoes:
                print(todo.split('.', 1)[1].strip())
                enumerated_todos.append(todo)
            write_todos(enumerated_todos, filepath=FILEPATH)
            break
        else:
            break


if __name__ == "__main__":
    #move_in_list_up()
    pass
