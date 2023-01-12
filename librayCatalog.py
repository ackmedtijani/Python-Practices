import sqlite3

items = []

class Catalog:
	pass

class LibraryItem:
	def __init__(self , title , subject):
		self.title = title
		self.subject = subject





class Book(LibraryItem):
	def __init__(self , title , subject , author , isbn , dds):
		LibraryItem.__init__(title , subject)
		self.author = author
		self.isbn = isbn
		self.dds = dds
		items.extend([title , subject , self.author , self.isbn , self.dds])


l1 = LibraryItem("Python Cookbook" , "Computer Science")

b1 = Book(l1 , "Computer Science", "Guido Van Rossum" , '1345-990' , 'CP45')
print(items)







