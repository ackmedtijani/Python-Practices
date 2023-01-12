from tkinter import *

window = Tk()

title_text = StringVar()
author_text = StringVar()
isbn_text = StringVar()
year_text = StringVar()

l1 = Label(window , text = "Title:")
l1.grid(row = 0 , column = 0 ,padx = 5 , pady = 4)

l1 = Label(window , text = "Year:")
l1.grid(row = 1 , column = 0 , padx = 5 ,pady = 4)

l1 = Label(window , text = "Author:")
l1.grid(row = 0 , column = 2 , padx = 5 , pady = 4)

l1 = Label(window , text = "ISBN:")
l1.grid(row = 1 , column = 2 ,  padx = 5 ,pady = 4)

e1 = Entry(window , width = 20 , textvariable = title_text)
e1.grid(row =  0 , column = 1)

e2 = Entry(window , width = 20 , textvariable = year_text)
e2.grid(row = 1 , column = 1 ,padx = 5, pady = 4)

e3 = Entry(window , width = 20 , textvariable = author_text)
e3.grid(row = 0 , column = 3 ,padx = 5)

e4 = Entry(window , width = 20 ,textvariable = isbn_text)
e4.grid(row = 1, column = 3 )

lb1=  Listbox(window  , height = 10 , width = 30)
lb1.grid(row = 2 , column = 0 ,padx = 5 , pady = 5 ,columnspan = 2 ,rowspan = 6)

sb1 = Scrollbar(window)
sb1.grid(row = 2 ,column = 2 , rowspan = 6)

lb1.configure(yscrollcommand = sb1.set)
sb1.configure(command = lb1.yview)



window.mainloop()