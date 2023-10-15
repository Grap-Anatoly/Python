from tkinter import *


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Hello world")
        self.minsize(300, 200)

        label = Label(text="Hello world!")
        label.pack()


root = Root()
root.mainloop()

