#!/usr/bin/python3

#9-10 Imported Restaurant

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name + ' ' + self.cuisine_type)
	
	def open_restaurant(self):
		print(self.restaurant_name + " is open")

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type): 
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'brocoli']
	
	def ice_flav(self):
		print(self.flavors)


