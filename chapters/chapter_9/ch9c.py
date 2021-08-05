#!/usr/bin/python3


#9-4 Number Served

class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 2
	

	def describe_restaurant(self):
		print(self.restaurant_name + ' ' + self.cuisine_type)
	
	def open_restaurant(self):
		print(self.restaurant_name + " is open")

	def num_serv(self):
		print(str(self.number_served) + " is the number of customers the restaurant has served")
	
	def set_number_served(self, no_serv):
		self.number_served = no_serv

	def increment_number_served(self, n_served):
		self.number_served += n_served

c = Restaurant('Bob', 'Italia')
c.describe_restaurant()
c.open_restaurant()

c.set_number_served(23)
c.num_serv()

c.increment_number_served(100)
c.num_serv()
