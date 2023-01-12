import re
import sys
from random import *
print()
string = eval(input("Enter the string: "))
def isallstring(string):
	if  string.isalnum() == True:
		print("Invalid Input")
		print("Only string with words")
		sys.exit()
	return 
isallstring(string)

def reverse(string):
	y = len(string) -2
	for i in range(1,len(string)-:
		string[i] = string[randint(1,len(y)-1)]
def  Typoglycemia(string):
	Pattern = re.compile(r'\w+')
	Message = Pattern.findall(string)
	for i in Message:
		if len(i) > 3 :
			reverse(i)
		print(i , end = " ")
Typoglycemia(string)


