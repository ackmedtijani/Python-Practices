#Tic Tac Toe Game 
from random import *
import sys

print()
print("Welcome to Tic Tac Toe Game".center(50))
print()
Player_1 = ""
Player_2 = ""


def GameStart():
	print('1 - Play against computer: ')
	print('2 - Play against Human: ')
	print()
	User = eval(input('Enter  your option (1 or 2): '))
	if User == 1:
		pass
	elif User == 2:
		return Player_1 , Player_2
GameStart()


def Userpick():
	x = randint(0,1)
	if x == 0:
		print()
		print('Player 1 chooses O')
		print('Player 2 chooses X')
		print()
		Player_1 = 'O'
		Player_2 = 'X'
	else:
		print()
		print('Player 2 chooses O')
		print('Player 1 chosses X')
		Player_1 = 'X'
		Player_2 = 'O'
		print()
	return Player_1 , Player_2
Userpick()


print("Indexes of the game".center(50))
def draw():
	print()
	print('           |             |             '.center(50))
	print('   top-l   |    top-m    |    top-r    '.center(50))
	print('           |             |             '.center(50))
	print('---------------------------------------'.center(50))
	print('           |             |             '.center(50))
	print('   mid-l   |    mid-m    |    mid-r    '.center(50))
	print('           |             |             '.center(50))
	print('---------------------------------------'.center(50))
	print('           |             |             '.center(50))
	print('   low-l   |    low-m    |    low-r    '.center(50))
	print('           |             |             '.center(50))
	print()
draw()
board = {'top-l':" ",'top-m':" ",'top-r':" ",'mid-l':" ",'mid-m': " ",'mid-r':" ",'low-l':" ",'low-m':" ",'low-r':" "}
def displayBoard(board):
	print()
	print('       |       |      ')
	print('  %s    |   %s   |   %s  '%(board['top-l'],board['top-m'],board['top-r']))
	print('       |       |      ')
	print('----------------------')
	print('       |       |      ')
	print('  %s    |   %s   |   %s  '%(board['mid-l'],board['mid-m'],board['mid-r']))
	print('       |       |      ')
	print('----------------------')
	print('       |       |      ')
	print('  %s    |   %s   |   %s  '%(board['low-l'],board['low-m'],board['low-r']))
	print('       |       |      ')
	print()

def keyitems(board,user):
	keyLists = []
	for i in board.keys():
		keyLists.append(i)
	for i in keyLists:
		if user == i:
			return 
	return False
def Winning(board):
	if (board['top-l']) == (board['top-m']) == (board['top-r']):
		print("%s has won" (board['top-l']))
		exit()
	elif(board['mid-l']) == (board['mid-m']) == (boarad['mid-r']):
		print("%s has won" (board['mid - m']))


		
def GamePlay():
	x1 , x2 = Userpick()
	turn = 'X'
	lists = []
	for i in range(9):
		if i == 0:
			print("Round One")
			print()
		if (turn == x1):
			print("Player 1's  turn ")
			print()
		else:
			print("Player 2's  turn")
			print()
		user = str(input("Make a your move: "))
		if keyitems(board , user) == False:
			print()
			print("Invalid index")
			print()
			draw()
			user = str(input("Make your move: "))
		for  i in  lists:
			if user == i:
				print()
				print("Try another index again.Index already used")
				print()
				draw()
				user = str(input("Make your move: "))
		board[user] = turn
		lists.append(user)
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
		displayBoard(board)
		
displayBoard(board)
GamePlay()





