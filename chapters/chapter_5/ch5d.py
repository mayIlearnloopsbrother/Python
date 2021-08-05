#!/usr/bin/python3

#5-8 Hello Admin

usernames = ['admin', 'bob', 'rob', 'mob', 'dob']

for username in usernames:
	if username == 'admin':
		print("hello " + username + ", would you like to see a status report?")
	else:
		print("hello " + username + ", thank you for logging in again.")

print("\n")
#5-9 No Users
usernames2 =[]

if usernames2:
	for username in usernames:
		print("hello " + username)
else:
	print("We need to find some users")
