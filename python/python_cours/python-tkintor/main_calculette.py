from tkinter import Button, Entry, Label, Tk, ttk
from tkinter import messagebox

# cree une frame (root)


def calcul():
    val1: float = float(entry_val_1.get())
    val2: float = float(entry_val_2.get())
    operator_selected = combobox.get()
    result = 0
    match(operator_selected):
        case '+':
            result = val1+val2
        case '-':
            result = val1-val2
        case '*':
            result = val1*val2
        case '/':
            result = val1/val2
    msg = messagebox.showinfo("Message", f"result = {result}")


#
# width_fullscreen = frame.winfo_screenwidth()
# height_fullscreen = frame.winfo_screenheight()
# frame
frame = Tk()
width = 600
height = 500
margin_right_box_btn = 150
frame.geometry(f"{width}x{height}")
frame.title("Calculette")

# label
label_val_1 = Label(frame, text="Valeur 1:")
label_val_1.place(x=margin_right_box_btn-50, y=50)
# input box
entry_val_1 = Entry(frame)
entry_val_1.place(x=margin_right_box_btn, y=50)
entry_val_1.insert(0, "0")


label_val_2 = Label(frame, text="Valeur 2:")
label_val_2.place(x=margin_right_box_btn-50, y=80)

entry_val_2 = Entry(frame)
entry_val_2.place(x=margin_right_box_btn, y=80)
entry_val_2.place(x=margin_right_box_btn, y=80)
entry_val_2.insert(0, "0")

# combobox
operations = ['+', '-', '*', '/']
combobox = ttk.Combobox(frame, values=operations)
combobox.place(x=margin_right_box_btn, y=120)
combobox.current(0)


# button
button = Button(frame, text="Calcul", command=calcul)
button.place(x=margin_right_box_btn, y=150)
label = Label(frame, text="Hello Tk")


frame.mainloop()
