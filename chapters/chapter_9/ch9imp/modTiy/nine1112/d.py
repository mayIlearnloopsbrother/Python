#!/usr/bin/python3

#9-11/12 Imported Admin/Multiple Modules

class User():

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(self.first_name + ' ' + self.last_name)

	def greet_user(self):
		print("Hello " + self.first_name)

