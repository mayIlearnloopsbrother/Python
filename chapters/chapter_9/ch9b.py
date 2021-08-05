#!/usr/bin/python3

#9-3 Users

class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def  describe_user(self):
		print(self.first_name + " " + self.last_name)
	
	def greet_user(self):
		print("hello " + self.first_name)


a = User('bob', 'paypal')
a.describe_user()
a.greet_user()

print("\n")

b = User('oliver', 'khan')
b.describe_user()
b.greet_user()
