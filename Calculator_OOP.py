class Calculator():
	def __init__(self , a , b):
		self._a = a
		self.__b = b
	def addition(self):
		self.__Total = self.__a + self.__b
		return self.__Total
	def subtraction(self):
		self.__Total = self.__a - self.__b
		return self.__Total
	def division(self):
		self.__Total = self.__a / self.__b
		return self.__Total
	def multiplication(self):
		self.__Total = self.__a * self.__b
		return self.__Total
	def square(self , s):
		self.__Total = self.__s ** 2
		return self.__Total
	def square_power(self , c , d):
		self.__Total = self.__c ** self.__d
		return self.__Total
		

