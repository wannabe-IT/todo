from asyncio import timeout

import functions
import PySimpleGUI as sg
import time


sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")

up_button = sg.Button(size=2, mouseover_colors="LightBlue2",key="Up", image_source="./img/up.png", image_size=(20, 20),)
down_button = sg.Button(size=2, mouseover_colors="LightBlue2",key="Down", image_source="./img/down.png")
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=(36, 1))
add_button = sg.Button(size=2, image_source="./img/add.png", mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(35, 10))
edit_button = sg.Button(size=2, image_source="./img/edit.png", mouseover_colors="LightBlue2",
                        tooltip="Edit Todo", key="Edit", )
complete_button = sg.Button(size=2, image_source="./img/complete.png", mouseover_colors="LightBlue2",
                            tooltip="Complete Todo", key="Complete")
save_button = sg.Button("Save")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box], [down_button, up_button, edit_button, complete_button,save_button, exit_button]],
                   font=("Helvetica", 20))

todos_original = functions.get_todos()
todos_completed = []
todos = functions.get_todos()

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Up":
            todo_index = values["todo"]
            #functions.move_in_list_up()
        case "Down":
            pass
        case "Add":
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20),
                         keep_on_top=True, modal=True)
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                todos_completed.append(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
                todos = functions.get_todos()
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "todos":
            try:
                window["todo"].update(value=values["todos"][0])
            except IndexError:
                sg.popup("Please add an item first.", font=("Helvetica", 20))
        case "Exit":
            confirm = sg.popup_yes_no("Want you to save your progress before exiting?",
                                      title="Exit confirmation",keep_on_top=True, modal=True, font=("Helvetica", 20))
            if confirm == "Yes":
                functions.write_todos(todos)
                break
            else:
                functions.write_todos(todos_original)
                break

        case "Save":
            confirm = sg.popup_yes_no("Are you sure you want to save your progress?",
                              title="Exit confirmation", keep_on_top=True, modal=True, font=("Helvetica", 20))
            todos = functions.get_todos()
            if confirm == "Yes":
                functions.write_todos(todos)
            else:
                pass


        case sg.WINDOW_CLOSED:
            break

window.close()