from tkinter import *

root = Tk()
B1 = Button(root , text = "Text")
B1.pack()

B1.bind('Button-1', (B1.flash()))
root.mainloop()