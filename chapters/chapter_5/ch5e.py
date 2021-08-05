#!/usr/bin/python3

#5-10 Checking Usernames

current_users = ['rob', 'bob', 'dave', 'jayce']
new_users = ['bob', 'hob', 'Rob']

for new_user in new_users:
	if new_user in current_users:
		print("the username " + new_user + " is available")
		print("the username " + new_user.title() + " is not available\n")
	else:
		print("the username " + new_user + " is not available\n")

