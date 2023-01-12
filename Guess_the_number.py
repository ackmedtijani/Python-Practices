from random import randrange
import sys

print()
print("Welcome to Guess the number".center(80))
print()
print("Player 1",end = "")
print("Player 2".rjust(70))

Value = randrange(0,100)

Player_1 = ""
Player_2 = ""
def random():
	x = randrange(0,1)
	print()
	if x == 0:
		turn  = 'Player 1'
		return turn
	else:
		turn = 'Player 2'
		return turn
random()

def Wining(User):
	if User == Value:
		return True
	if User in range(Value , 100):
		if User  in range(Value , Value + 11):
			print('Close')
		else:
			print("Too High")
	elif User  in range(0 , Value ):
		if User  in range(Value - 10 , Value):
			print('Close')
		else:
			print("Too Low")

def player():
	turn = random()
	while True:
		print()
		print("%s's turn" % (turn))
		print()
		User = int(input("Enter the message: "))
		if User  not in range(0,100):
			print()
			print("Invalid Input. Value out of range")
			User = int(input("Enter the messages: "))
		if Wining(User) == True:
			print()
			print("%s wins" % (turn))
			sys,exit()	
		if turn == 'Player 1':
			turn = 'Player 2'
		elif turn == 'Player 2':
			turn = 'Player 1'
player()

	




