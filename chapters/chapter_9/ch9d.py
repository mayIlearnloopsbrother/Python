#!/usr/bin/python3

#9-5 Login Attempts
class User():
	
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		print(self.first_name + ' ' + self.last_name)

	def greet_user(self):
		print("hello " + self.first_name + ' ' + self.last_name)

	def log_attempts(self):
		print("login attempts: " + str(self.login_attempts))
 
	def increment_login_attempts(self, login):
		self.login_attempts += login

	def reset_login_attempts(self):
		self.login_attempts = 0

c = User('bob', 'jim')
c.describe_user()
c.greet_user()

c.increment_login_attempts(5)
c.log_attempts()

c.reset_login_attempts()
c.log_attempts()
