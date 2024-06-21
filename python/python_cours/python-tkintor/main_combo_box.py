
from tkinter import ANCHOR, END, Button, Tk, ttk
from tkinter import messagebox


def select_one():
  msg=messagebox.showinfo( "Message", f"valeur selectionner = {combobox.get()}")



frame = Tk()
width= 600
height= 500
margin_right_box_btn = 150
frame.geometry(f"{width}x{height}")
frame.title("Calculette")

language=['java','c++','python']
combobox = ttk.Combobox(frame,values=language)
combobox.pack()


button4 = Button(frame, text ="Select one", command = select_one)
button4.pack()

frame.mainloop()
