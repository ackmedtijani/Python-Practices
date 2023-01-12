import shelve
from datetime import datetime , time  
import  re 

###########################################
# Airline Reservation Application         #
# Written by Oboirien Ahmed Tijani        #
###########################################
def economy():

	all_flights = [['Cairo' , 'Arik' , '2017/11/23 21:00', 50000 , 90, 'Avaliable'] ,
	['Dubai' , 'Fly Emirates' , '2017/4/2 09:00' , 70000  , 56 , 'Avaliable'] , 
	['London', 'Virgin Airlines' , '2017/6/5 08:00' , 90000 , 70 , 'Avaliable' ],
	['New York' , 'Virgin Airlines' , '2017/3/23 13:30' , 100000 , 100 , 'Avaliable']]

	return all_flights

def firstClass():
	all_flights = [['Cairo' , 'Arik' , '2017/11/23 ', 100000 , 45 , 'Avaliable'] ,
	['Dubai' , 'Fly Emirates' , '2017/4/2' , 170000  , 56 , 'Avaliable'] , 
	['London', 'Virgin Airlines' , '2017/6/5' , 190000 , 70 , 'Avaliable' ],
	['New York' , 'Virgin Airlines' , '2017/3/23' , 200000 , 87 , 'Avaliable']]

	return all_flights

def secondClass():
	all_flights = [['Cairo' , 'Arik' , '2017/11/23 ', 70000 ,  'Avaliable' , 60 ] ,
	['Dubai' , 'Fly Emirates' , '2017/4/2' , 10000   , 'Avaliable' , 65] , 
	['London', 'Virgin Airlines' , '2017/6/5' , 130000 ,  'Avaliable' , 81 ],
	['New York' , 'Virgin Airlines' , '2017/3/23' , 120000 ,'Avaliable' , 92]]

	return all_flights
#def display():
#	lists = ["Destination" , "Airline" , "Date and time of flight" , "Ticket Price" , "Avaliablity"]
#	print()
#	print(lists[0].rjust(11), end = " ")
#	for i in range(1 , len(lists)):
#		print("|" , end = " ")
#		print(lists[i].center(20) , end = " ")
#	print()
#	print("============" * 7)


def displays(lst):
	print()
	for i in range(len(lst)):
		if (i == 0):
			print("Destination:				{}".format(str(lst[i])))
			print()
		elif (i == 1):
			print("Airline:  				{}".format(str(lst[i])))
			print()
		elif (i == 2):
			print("Date and time of flight:		{}".format(str(lst[i])))
			print()
		elif(i == 3):
			print("Ticket Price 				{}".format(str(lst[i])))
			print()
		elif(i == 4):
			print("Avaliability:				{}".format(str(lst[i])))
			print()
	print()
	print("========" * 7)


class FirstClass():
	all_flights = firstClass()
	shelfFile = shelve.open('FirstClass' , writeback = True)
	

	def __init__(self , destination , Airline ,Date_of_flight , TicketPrice , PassengerSpace , Avaliable):
		self.data = [destination , Airline , Date_of_flight , TicketPrice , PassengerSpace , Avaliable]
		FirstClass.all_flights.append(self.data)

	@classmethod
	def display(cls , destination = None , Airline = None , Date_of_flight = None , TicketPrice = None , Avaliable = None):
		print()
		print("FLIGHT DETAILS".center(70))
		print("======" * 10)
		for i in FirstClass.all_flights:
			displays(i)

	@classmethod
	def remove(self , destination , Airline , Date_of_flight , TicketPrice):
		for i in FirstClass.all_flights:
			i.remove()

	shelfFile['1'] = all_flights
		
	shelfFile.close()

class SecondClass():
	
	all_flights = secondClass()
	shelfFile = shelve.open('SecondClass' , writeback = True)
	shelfFile['1'] = all_flights

	def __init__(self , destination , Airline , Date_of_flight , TicketPrice , PassengerSpace , Avaliability):
		self.data = [destination , Airline ,Date_of_flight , TicketPrice , PassengerSpace , Avaliability]
		all_flights.append(self.data)


	@classmethod
	def display(cls , destination = None , Airline = None , Date_of_flight = None , TicketPrice = None , Avaliable = None):
		print()
		print("FLIGHT DETAILS".center(70))
		print("======" * 10)
		for i in FirstClass.all_flights:
			displays(i)

	shelfFile.close()

class Economy():


	all_flights = economy()
	shelfFile = shelve.open('Economy' ,writeback = True)
	

	def __init__(self , destination , Airline , Date_of_flight , TicketPrice ,Avaliability ,PassengerSpace ):
		self.data = [destination , Airline , Date_of_flight , TicketPrice ,  Avaliability , PassengerSpace]
		all_flights.append(self.data)

	@classmethod
	def display(cls , destination = None , Airline = None , Date_of_flight = None , TicketPrice = None , Avaliable = None):
		print()
		print("FLIGHT DETAILS".center(70))
		print("======" * 10)
		for i in FirstClass.all_flights:
			displays(i)

	shelfFile['1'] = all_flights
	shelfFile.close()

FirstClass.display()


def bubble_sort(A):
	for i in range(len(A) - 1):
		for j in range(len(A) - 1 - i):
			if A[j+1] < A[j]:
				A[j] , A[j+1] = A[j+1], A[j]
	print(A) 
bubble_sort([6 , 1 , 3 , 4 , 2 ,5 , 7])

def selection_sort(A):
	for i in  range(len(A) - 1):
		j = i
		mini = i
		for x in  range(i + 1  , len(A)):
			if A[mini] >= A[x]:
				mini = x
		A[j] , A[mini] = A[mini] , A[j]
	print(A)
selection_sort([3, 7 , 6 ,4 , 2 ,5 ,1])

def merge(a , b):
	c = []
	while len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0])
		else:
			c.append(b[0])
			b.remove(b[0])
	if len(a) == 0:
		c += b
	else:
		c += a
	return c

def mergesort(x):
	if len(x) == 0 or len(x) == 1:
		return x
	else:
		middle = len(x) // 2
		a = mergesort(x[: middle])
		b = mergesort(x[middle :])
		return merge(a , b)

print(mergesort([1 , 43 ,3 ,34 ,52 ,6 , 7 ,8 , 4  , 2 ,10 , 16 , 19  , 45]))

def insertion_sort(s):
	for i in range(1, len(s)):
		val = s[i]
		j = i - 1
		while (j >= 0) and (s[j] >= val):
			s[j+1] = s[j]
			j = j - 1
		s[j + 1] = val
	print(s)

insertion_sort([3, 7 , 6 ,4 , 2 ,5 ,1]) 

def quick_sort(s):
	less = []
	equal = []
	greater = []

	if len(s) > 1:
		pivot = s[0]
		for x in s:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return quick_sort(less) + equal + quick_sort(greater)				


	  
	else:
		return s


quick_sort([3, 7 , 6 ,4 , 2 ,5 ,1])