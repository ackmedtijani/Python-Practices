from tkinter import *
from tkinter import messagebox

root = Tk()
root.configure(background = '#4D4D4D')

equa = ""
equation = StringVar()


calculation = Entry(root , width = 20 , textvariable = equation)
equation.set("")

calculation.grid(row = 0 , column = 0 , rowspan = 2, columnspan = 4  , pady = 2)


def btnPress(num):
	global equa
	equa = equa + str(num)
	equation.set(equa)


def AnsPress():
	evals = str(eval(equa))
	equation.set(evals)

def delete():
	global equa
	if len(equa) > 0:
		equa = ""
		equation.set(equa)
Button1 = Button(root , text = "1" , command = lambda : btnPress(1))
Button1.grid(row = 2 , column = 0  , sticky = 'ew' , pady = 5)

Button2 = Button(root , text = "2" , command = lambda : btnPress(2))
Button2.grid(row = 2 , column = 1 , sticky = 'ew')

Button3 = Button(root , text = "3" , command = lambda : btnPress(3))
Button3.grid(row = 2 , column = 2 , sticky = 'ew')

ButtonDiv = Button(root , text = '/' , command = lambda : btnPress('/'))
ButtonDiv.grid(row = 2, column = 3 , sticky = 'ew')

Button4 = Button(root , text = "4" , command = lambda : btnPress(4))
Button4.grid(row = 3 , column = 0 , sticky = 'ew')

Button5 = Button(root , text = "5" , command = lambda : btnPress(5))
Button5.grid(row = 3 , column = 1  , sticky = 'ew' , pady = 5)

Button6 = Button(root , text = "6" , command = lambda : btnPress(6))
Button6.grid(row = 3 , column = 2  , sticky = 'ew' , pady = 5)

ButtonMult = Button(root , text = "*" , command = lambda : btnPress('*'))
ButtonMult.grid(row = 3 , column = 3  , sticky = 'ew' , pady = 5)

Button7 = Button(root , text = "7" , command = lambda : btnPress(7))
Button7.grid(row = 4 , column = 0  , sticky = 'ew' , pady = 5)

Button8 = Button(root , text = "8" , command = lambda : btnPress(8))
Button8.grid(row = 4 , column = 1  , sticky = 'ew' , pady = 5)

Button9 = Button(root , text = "9" , command = lambda : btnPress(9))
Button9.grid(row = 4 , column = 2 , sticky = 'ew' , pady = 5)

ButtonPlus = Button(root , text = "+" , command = lambda : btnPress('+'))
ButtonPlus.grid(row = 4 , column = 3  , sticky = 'ew' , pady = 5)

ButtonZero = Button(root , text = "0" , command = lambda : btnPress(0))
ButtonZero.grid(row = 5 , column = 0  , sticky = 'ew' , pady = 5)

ButtonMinus = Button(root , text = "-" , command = lambda : btnPress('-'))
ButtonMinus.grid(row = 5 , column = 1  , sticky = 'ew' , pady = 5)

ButtonDot = Button(root , text = "." , command = lambda : btnPress('.'))
ButtonDot.grid(row = 5 , column = 2  , sticky = 'ew' , pady = 5)

ButtonClear = Button(root , text = 'C' , command = delete)
ButtonClear.grid(row = 5 , column = 3 , sticky = 'ew' , pady = 5)

ButtonAnswer = Button(root , text = 'Ans' , command = AnsPress)
ButtonAnswer.grid(row = 6 , column = 1  , sticky = 'ew' , pady = 5)


root.mainloop()    