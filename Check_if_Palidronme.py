print()
string = str(input("Enter the string: "))
x = len(string)
y = x -1 
def ifpalidronme(string):
	string2 = ""
	count = 0
	for i in range(y,-1,-1):
		string2 = string2 + string[i]
	if string2 == string:
		return True
print()
print(ifpalidronme(string))



