#!/usr/bin/python3

#9-1/2 Restaurant
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name + " " + self.cuisine_type)
	
	def open_restaurant(self):
		print(self.restaurant_name + " is open")

my_restaurant = Restaurant('bob finest', 'italia')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant() 

your_restaurant = Restaurant('jims finest', 'jtalia')
your_restaurant.describe_restaurant()

her_restaurant = Restaurant('kims finest', 'ktalia')
her_restaurant.describe_restaurant()
