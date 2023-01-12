import shelve
from datetime import datetime , time
import  re 
 
def economy():

	all_flights = [['Cairo' , 'Arik' , '2017/11/23 21:00', 50000 , 90 , 'Avaliable'] ,
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
	all_flights = [['Cairo' , 'Arik' , '2017/11/23 ', 70000 , 60 , 'Avaliable'] ,
	['Dubai' , 'Fly Emirates' , '2017/4/2' , 10000  , 65 , 'Avaliable'] , 
	['London', 'Virgin Airlines' , '2017/6/5' , 130000 , 81 , 'Avaliable' ],
	['New York' , 'Virgin Airlines' , '2017/3/23' , 120000 , 92 , 'Avaliable']]

	return all_flights
def display():
	print("{0} {1} {2} {3} {3} {4}".format("Destination" , "Airline" , "Date and Time of Flight" , "Ticket Price" , "Passenger Space" , "Avaliability"))

display()
class FirstClass():

	all_flights = firstClass()

	def __init__(self , destination , Airline ,Date_of_flight , TicketPrice , PassengerSpace , Avaliable):
		self.data = [destination , Airline , Date_of_flight , TicketPrice , PassengerSpace , Avaliable]
		all_flights.append(self.data)

	def display(self , destination , Airline = None , Date_of_flight = None , TicketPrice = None , Avaliable = None):
		for i in range(len(all_flights)):
			for j in range(len(all_flights[i])):
				pass







class SecondClass():
	pass

class Economy():
	pass