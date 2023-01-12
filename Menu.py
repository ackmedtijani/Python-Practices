from ToDo import NoteBook , Note

class Menu():

	def __init__(self):
		self.choices = { '1': self.creatNote, 
		'2': self.createNoteBook,
		'3': self.saveNotebook,
		'4': self.AddNote,
		'5': self.ModifyNote,
		'6': self.SearchNote,
		'7': self.DeleteNote,
		'8': self.DeleteNoteBook}

	def display(self):
		print('''
			NoteBook Menu

		1.Create a Note
		2.Create a Notebook
		3.Save to a Notebook
		4.Add Note
		5.Modify Note
		6.Search for Note
		7.Delete a Note
		8.Delete your Notebook

		''')

	def run(self):
		self.display()
		choice = str(input("Enter you choice: "))
		action = self.choices.get(choice)

		if action:
			action()

		else:
			print("{0} you have entered an Invalid Operand.".format(choice))

	def 


if __name__ ==  "__main__":
	Menu().run()