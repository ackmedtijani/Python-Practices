import math 
print()
print()
print("Welcome to Calculator".center(70))
print()
print("Peform basic and scientific operations".center(80))
print()
print("0 - Basic Operations",end = '')
print("1 - Scientific Operations".center(90),end = '')
print()
def Basic():
	print(end = "")
	print("1 - Addition(+)",end = " ")
	print("2 - Subtraction(-)".center(90),end = " ")
	print()
	print("3 - Multiplication(*)",end = " ")
	print("4 - Division(/)".center(80))
	print("5 - Square(**)",end = ' ')
	print("6 - Squareroot(sqrt)".center(90),end = " ")
	print()
def scientific():
	print()
	print("8 - sin(x)",end = '')
	print("9 - cos(x)".center(40),end = '')
	print("10 - tan(x)".rjust(10),end = '')
	print()

User = str(input("Enter your pick: "))
print()
print()
def pick(User):
	if int(User) == 1:
		scientific()
	elif int(User) == 0:
		Basic()
pick(User)

def multiplication(a , b):
	Total = a * b
	return Total
def Adddition(a , b):
	Total = a + b
	return Total
def Subtraction(a , b):
	Total = a - b
	return Total
def Division(a , b):
	Total = a / b
	return Total
def Square (a):
	Total = a**2
	return Total
def SquareRoot(a):
	Total = sqrt(a):
	return Total

def calculation():
	while True:
		print(end = '')
		User_1 = str(input())
		print(end = "")
		Operand = str(input())
		print(end = "")
		User_3 = str(input())
		if User_1 == 'Ans':
			x = 
		if 

