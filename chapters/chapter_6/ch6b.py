#!/usr/bin/python3

#6-6 Polling

favorite_languages = {
	'jen': 'python',
	'sarah': 'c', 
	'edward': 'ruby',
	'phil': 'python',
	}
people = ['jen', 'bob', 'edward', 'hope']
for name in favorite_languages.keys():
	print("\n" + name.title())
	
	if name in people:
		print("hi " + name.title() + " thanks for polling ")
	else:
		print("if you haven't poll please do so \n") 
