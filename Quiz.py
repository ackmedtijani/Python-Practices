from tkinter import *

window = Tk()

def mesBox():
	print("Success")
	t1.insert(END , e1_value.get())


b1 = Button(window , text = "Execute" , command = mesBox)
b1.grid(row = 0 , column = 0)

e1_value = StringVar()
e1 = Entry(window , textvariable = e1_value)
e1.grid(row = 0 , column = 1)

t1 = Text(window , height = 20 , width = 30)
t1.grid(row = 0 , column = 3)

window.mainloop()