import os , os.path , sys
print()
print("1 - Create a New Note")
print("2 - Open an existing Note")
print("3 - Delete Note")
print()
try:
    Move = int(input("Enter the your pick: "))
except TypeError:
	print('Invalid input')
os.chdir('C:\\Users\\pc\\Documents\\Notepad')
def Open():
	print()
	File = str(input("Enter the name of file: "))
	File = File + '.txt'
	return File
def exists():
	x = Open()
	if os.path.isfile(x):
		Files = open(x , 'r')
		Files = Files.read()
		return Files , x
	else:
		print()
		print('File Missing')
def Re_exists():
	x = Open()
	if os.path.isfile(x):
		print()
		print('File already availiable.Create another unique file')
		sys.exit()
	else:
		Files = open(x , 'w')
		return Files
def Note():
	print()
	if Move == 1:
		Files = Re_exists()
		string = str(input())
		Files.write(string)
		Files.close()
	elif Move == 2:
		Content , Filename = exists()
		print(Content)
	elif Move == 3:
		try:
			x = Open()
			os.unlink(x)
		except FileNotFoundError:
			print()
			print('File does not exist')
Note()






    
		