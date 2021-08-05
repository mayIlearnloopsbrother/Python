#!/usr/bin/python3

alien_color = 'green'

if alien_color == 'green':
	print("you shot down green alien: 5 points")

alien_color2 = 'yellow'

if alien_color2 == 'green':
	print("5 points")

alien_color3 = 'red'

if alien_color3 == 'green':
	print("5 points")
else:
	print("You shot alien that isn't green: 10 points")


if alien_color == 'green':
	print("You shot green alien: 5 points")
elif alien_color == 'yellow':
	print("you shot yellow alien: 10 points")
else:
	print("15 points for shooting down red alien")

