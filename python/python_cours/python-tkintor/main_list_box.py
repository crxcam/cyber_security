from tkinter import ANCHOR, END, Button, Entry, Label, Listbox, Tk
from tkinter import messagebox

# cree une frame (root)

def somme():
   val1:float = float(entry_val_1.get())
   val2:float = float(entry_val_2.get())
   somme = val1+val2
   msg=messagebox.showinfo( "Message", f"somme = {somme}")

def delete_one():
   listbox.delete(ANCHOR)

def delete_all():
   listbox.delete(0,END)

def select_one():
  msg=messagebox.showinfo( "Message", f"selectionner = {listbox.get(ANCHOR)}")

def select_many():
   selected= listbox.curselection()
   result=''
   for el in selected:
      result += listbox.get(el) + ""
   msg=messagebox.showinfo( "Message", f"selection multiple: = {result}")




#
#width_fullscreen = frame.winfo_screenwidth()
#height_fullscreen = frame.winfo_screenheight()




#frame
frame = Tk()
width= 600
height= 500
margin_right_box_btn = 150
frame.geometry(f"{width}x{height}")
frame.title("Calculette")

#COLUMN 1 
#listbox
language=['java','c++','python']
listbox= Listbox(frame,selectmode='extended')
for el in language:
   listbox.insert(END,el)
listbox.grid(column=0,row=0)

#button
button1 = Button(frame, text ="Delete one", command = delete_one)
button1.grid(column=0,row=10)

button2 = Button(frame, text ="Delete all", command = delete_all)
button2.grid(column=0,row=12)

button2 = Button(frame, text ="Delete all",command=delete_all)
button2.grid(column=0,row=12)

button3 = Button(frame, text ="Select one", command = select_one)
button3.grid(column=0,row=14)

button4 = Button(frame, text ="Select many", command = select_many)
button4.grid(column=0,row=16)



# input box
entry_val_1 = Entry(frame,text="Valuer 1")
entry_val_1.place(x=margin_right_box_btn,y=50)
entry_val_1.insert(0,"0")

label_val_1 = Label(frame,text="Valuer 1:")
label_val_1.place(x=margin_right_box_btn,y=10)
entry_val_2 = Entry(frame)
entry_val_2.place(x=margin_right_box_btn,y=80)
entry_val_2.place(x=margin_right_box_btn,y=80)
entry_val_2.insert(0,"0")

#button
button = Button(frame, text ="Calcul somme", command = somme)
button.place(x=margin_right_box_btn,y=120)








frame.mainloop()


