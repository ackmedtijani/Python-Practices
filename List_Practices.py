spam = ['apples','bananas','tofu','cats']

def list(spam):
	string = ""
	for i in range(0,len(spam)):
		if i == len(spam)-1:
			string = string + " and "+str(spam[i]).capitalize()
		else:
			string = string + str(spam[i]).capitalize() + ", "
	return string
print(list(spam))

grid = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24,25]]
print()
def grids(grid):
	string = ""
	for i in range(len(grid)):
		x = len(grid[i])
		for j in range(x):
			print(grid[i][j] ,end = " ")
			if j == x-1:
				print()
grids(grid)

dictionary = {'rope' : 1 , 'torch': 6 ,'gold coin': 42, 'dagger': 1, 'arrow': 12}

print()

def displayInventory(dictionary):
	print("Inventory: ")
	print()
	x = 0
	for i , j in dictionary.items():
		print("%i  %s" % (j , i))
		x = x + j
	print()
	print("Total number of items: %i" % (x))
displayInventory(dictionary)

print()

Inventory = {'gold coin': 42,'rope': 1}
addItems = ['gold coin','dagger','gold coin','gold coin','ruby']
def addToInventory(Inventory , addItems):
	count = {}
	count_1 = {}
	for i in addItems:
		count.setdefault(i , 0)
		count[i] = count[i] + 1
	return count 
print(addToInventory(Inventory , addItems))



		

