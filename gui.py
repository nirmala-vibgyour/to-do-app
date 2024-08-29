import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# [label, input_box] in a row. a list eqv to a row.
window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])

while True:
    # displays the window
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
