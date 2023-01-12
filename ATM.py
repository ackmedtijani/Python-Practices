class BankAccount():
	NumOfBankAccounts = 0
	def __init__(self , name , number , ssn , balance ):
		self.name = name
		if len(str(number)) == 10:
			self.number = number
		else:
			print("Invalid Account Number.Length of Account Number must be 10")
		self.ssn = ssn
		self.balance = balance
		self.minimumBal = 1000
		self.active = True

	def set_active(self , act):
		self.__active = act
	def is_active():
		return self.__active
	def withdraw(self , amount):
		if is_active() and (self.__balance - self.__amount >= self.__minimumBal):
			self.__balance -= self.__amount
			return self.__amount 
		if is_active() == False:
			print('Account inactive')
		if self.__balance - self.__amount < self.__minimumBal:
			print('Insufficient Account')

	def deposit(self , amount):
		if  is_active():
			self.__balance += self.__amount
			return self.__balance
		else:
			print('Account inactive')
	def NumOfBankAccounts(self):
		return NumOfBankAccount
			
class ATM(BankAccount):
	def __init__(self , name , number , ssn , balance , pin):
		super().__init__(name , number , ssn , balance)
		self.pin = pin



Acc1 = BankAccount("Tijani Oboirien",3102381213,2345,500000)
Atm1 = ATM("Tijani Oboirien",3102381213,2345,5000000, 2402)









