#!/usr/bin/python3

#9-11/12 Imported Admin/Multiple Modules

from d import User

class Admin(User):
		def __init__(self, first_name, last_name):
			super().__init__(first_name, last_name)
			self.priv = Privileges()				

class Privileges():
	def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
		self.privileges = privileges
 
	def show_privileges(self):
			print(self.privileges)



