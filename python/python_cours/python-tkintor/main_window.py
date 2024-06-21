from tkinter import Button, Tk


class MyWindow(Tk):

    def __init__(self):
        # On appelle le constructeur parent
        super().__init__()

        button1 = Button(self, text="Button 1")
        button1.grid(column=0, row=0)

        button2 = Button(self, text="Button 2")
        button2.grid(column=1, row=0)

        button3 = Button(self, text="Button 3")
        button3.grid(column=0, row=1)

        button4 = Button(self, text="Button 4")
        button4.grid(column=1, row=1)

        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Positionnement de widgets via grid")

window = MyWindow()
window.mainloop()