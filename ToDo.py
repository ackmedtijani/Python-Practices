import os , os.path
from datetime import datetime , time 
import shutil
import sys

os.chdir("C:\\Users\\pc\\Documents\\Notepad")

class Note():

	
	def __init__(self , name , expDate , text = ''' ''' ,title = ''' '''):
		if os.path.isfile(name + '.txt'):
			self.file = open(name + '.txt' , 'w')
		else:
			self.file = open(name + '.txt' , 'w')

		self.text = text
		self.date = datetime.strptime(expDate , "%Y/%m/%d")
		self.file.write("Expiration Date: {}".format(expDate))
		self.title = title
		if len(self.title) != 0:
			self.file.write('''\n\nTitle: {}'''.format(self.title))
		if len(self.text) != 0:
			self.file.write('''\n\nContent:\n\n{}'''.format(self.text))

	def modify(self , text):
		self.file.write('''\n''' + text)
		
	@classmethod
	def delete(cls,name):
		try:
			return os.remove(name + '.txt')
		except FileNotFoundError:
			print("Already Deleted")

	def deletes(self , name):
		try:
			return os.remove(name + '.txt')
		except FileNotFoundError:
			print("Already Deleted")



class NoteBook():

	def __init__(self , Name , Note = None):
		if not os.path.isdir("C:\\Users\\pc\\Documents\\ToDo\\" + Name):
			self.Nam = os.mkdir("C:\\Users\\pc\\Documents\\ToDo\\" + Name)
			self.Name = "C:\\Users\\pc\\Documents\\ToDo\\" + Name
		else:
			print("Already Avaliable")
			sys.exit()
		if Note != None:
			self.Note = Note
			shutil.move( self.Name , self.Note)

	@classmethod
	def add(cls , Note , NoteBook):
		try:
			return shutil.move(Note + '.txt' , "C:\\Users\\pc\\Documents\\ToDo\\" + NoteBook)

		except:
			print("Already Exist")


	def addNotes(self , note = []):
		if self.note != []:
			try:
				for i in self.note:
					shutil.move(self.Name , self.note)
			except:
				pass

	def modify(self , Note):
		try:
			for i in self.Name:
				if i == Note:
					file = open(Note , 'w')
					input = str(input("Enter your text: "))
		except:
			pass


	@classmethod
	def delete(cls,name):
		try:
			return os.remove(name + '.txt')
		except FileNotFoundError:
			print("Already Deleted")

	@classmethod
	def deletes(cls , NoteBook):
		cls.NoteBook = "C:\\Users\\pc\\Documents\\ToDo\\" + NoteBook
		return rmdir(cls.NoteBook)
    

	def search(self , Note):

		try:
			for i in os.listdir(self.Name):
				if i == Note:
					return "Found"
			return 'Not Found'

		except:
			print("Invalid Input")

	@classmethod 
	def open(cls , NoteBook):
		pass
	@classmethod	
	def modify(cls, Note , NoteBook):
		cls.NoteBook = "C:\\Users\\pc\\Documents\\ToDo\\" + NoteBook
		cls.Note = Note + '.txt'
		try:
			for i in os.listdir(cls.NoteBook):
				if i == cls.Note:
					return "Found"
			return "Not Found"
		except:
			pass

print(NoteBook.modify("Tues" , "FirstNoteBook"))


