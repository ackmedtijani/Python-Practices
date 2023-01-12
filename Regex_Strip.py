class Employee:
	num_of_emps = 0
	raise_amount = 1.05
	def __init__(self , first , last , pay): 
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + "@acompany.com"
		Employee.num_of_emps += 1

	def fullname(self):
		return "{} {}".format(self.first , self.last)


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls , amount):
		  cls.raise_amount = amount

	@classmethod 
	def new__init__(cls , emp_str):
		first ,last , pay = emp_str.split(',')
		return cls(first , last , pay)
	@staticmethod
	def is_workday(day):
		if day.weekday == 5 or day.weekday == 6:
			return False
		return True
	def __repr__(self):
		return "Employee('{}' , '{}' , '{}')".format(self.first , self.last , self.pay)

	def __str__(self):
		return "{} - {}".format(self.fullname(),self.email)

	def __add__(self , me):
		return self.pay + me.pay

class Developer(Employee):
	raise_amt = 1.10
	def __init__(self , first , last , pay , prog_lang):
	    super().__init__(first , last , pay)
	    self.prog_lang = prog_lang 

class Manager(Employee):
	raise_amt = 1.20
	def __init__(self , first , last , pay , employees = None):
	    super().__init__(first , last , pay)
	    if employees is None:
	    	self.employees = []
	    else:
	    	self.employees = employees

	def add_emp(self , emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self , emp):
		if emp in  self.employees:
			self.employees.remove(emp)
	def print_emp(self):
		for i in self.employees:
			print("--->",i.fullname())


emp1 = Employee("Oboirien","Tijani", 56000)
emp2 = Employee("Tester","User",6000)

dev1 = Developer("Ajao", "Jumat", 70000,"Python")
dev2 = Developer("Olarenwaju" , "Ahmed",7000 , "Java")

mgr1 = Manager("Odedairo","Akin",10000,[dev1 , dev2])
mgr1.print_emp()
print(mgr1.employees)
print(isinstance(mgr1 , Manager))
print(Employee.num_of_emps)

print(emp1)
print(emp1.__repr__())
print(repr(emp1))
print(emp1 + emp2)

emp1 .first = "Jagban"
emp1.fullname()