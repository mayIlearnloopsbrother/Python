#!/usr/bin/python3

#7-4 Pizza Toppings
info = "enter pizza toppings "
info += "\n'quit' to finish: "

topps = ""
while topps != 'quit':
	topps = input(info)

	if topps != 'quit':
		print("\nAdding " + topps + " to your pizza\n")

print("\n")
#7-5 Movie Tickets

age = input("age? ")
age = int(age)

if age < 3:
	print("ticket is free")
elif age < 12:
	print("$10 for a ticket")
elif age > 12:
	print("$15 for a ticket")	
