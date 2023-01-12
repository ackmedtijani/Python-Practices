class Agent():
	pass



class Property():
	all_properties = []
	def __init__(self , square_feet = " " , beds = " " , baths = " "):
		self.square_feet = square_feet
		self.beds = beds
		self.baths = baths

	def display(self):
		print('''PROPERTY DETAILS
==========================================

1. Square Footage: {}
2. Bedrooms: {}
3. Bathromms: {}'''.format(self.square_feet , self.beds , self.baths))


class House(Property):

	def __init__(self , )