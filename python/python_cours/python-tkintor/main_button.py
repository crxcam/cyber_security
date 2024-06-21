from tkinter import Button, Entry, Label, Tk
from tkinter import messagebox

# cree une frame (root)

def helloCallBack():
   msg=messagebox.showinfo( "Message", texte,)



#
#width_fullscreen = frame.winfo_screenwidth()
#height_fullscreen = frame.winfo_screenheight()

#frame
frame = Tk()
width= 600
height= 500
frame.geometry(f"{width}x{height}")
frame.title("First frame")

# input box
entry = Entry(frame)
entry.grid(column=0,row=0)
texte = entry.get()

#button
button = Button(frame, text ="Hello", command = helloCallBack)
button.place(x=50,y=50)
label = Label(frame, text="Hello Tk")
#button.pack()

#label.pack()


frame.mainloop()


