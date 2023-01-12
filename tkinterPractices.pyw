from tkinter import *

window = Tk()
window.title("Mass Converter")

e1_value = StringVar()


def grams():
	value = float(e1_value.get()) * 1000
	t1.insert(END , value)

def Pounds():
	value = float(e1_value.get()) * 2.20462
	t1.insert(END , value)

def Ounces():
	value = float(e1_value.get()) * 35.274
	t1.insert(END ,value)

l1 = Label(window , text = "Input Value:")
l1.grid(row = 0 , column = 0 ,padx = 2 , pady = 10)

e1 = Entry(window , width = 40 ,textvariable = e1_value)
e1.grid(row = 0 ,column = 1  , padx = 2 , pady = 20)

b1 = Button(window , text = "Convert to Pounds" ,command = Pounds , relief = RIDGE)
b1.grid(row = 0 , column = 11, padx = 10 )

l2 = Label(window , text = "Output Value:")
l2.grid(row = 1 , column = 0 , padx = 2 , pady = 10)

t1 = Text(window , height = 1 , width = 30)
t1.grid(row = 1 , column = 1 , padx = 2)

b2 = Button(window , text = "Convert to Ounce" ,command = Ounces , relief = RIDGE )
b2.grid(row = 1 ,column = 11)

b3 = Button(window , text = "Convert to grams" ,command = grams , relief = RIDGE)
b3.grid(row = 2,column = 11 ,padx = 2 , pady = 10)

window.mainloop()