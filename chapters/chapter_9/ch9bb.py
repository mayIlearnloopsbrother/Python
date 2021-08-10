#!/usr/bin/python3

#9-7/8 Admin

class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(self.first_name + ' ' + self.last_name)

	def greet_user(self):
		print("Hello " + self.first_name)

class Admin(User):
		def __init__(self, first_name, last_name):
			super().__init__(first_name, last_name)
			self.priv = Privileges()				

class Privileges():
	def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
		self.privileges = privileges
 
	def show_privileges(self):
			print(self.privileges)



c = Admin('Bob', 'penni')
c.describe_user()
c.greet_user()
c.priv.show_privileges()
