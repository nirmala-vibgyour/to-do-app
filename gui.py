import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# [label, input_box] in a row. a list eqv to a row.
window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])

# displays the window
window.read()

# closes the window when user closes it.
window.close()

