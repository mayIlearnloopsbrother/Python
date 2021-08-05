#!/usr/bin/python3

#7-1 Rental Car
car = input("what rental car would you like ")

print("let me see if i can find you a " + car.title())

print("\n")

#7-2 Restaurant Seating
user = input("how many people on the dinner group? ")
no_people = int(user)

if no_people < 8:
	print("table RRREAAADDYYY")
elif no_people < 50:
	print("whole restaurant booked")
elif no_people > 50:
	print("are you freaking kidding me")
else:
	print("they have to wait")

print("\n")

#7-3 Multiples of Ten

num = input("gimme numbah ")
num = int(num)

if num % 2 == 0:
	print(str(num) + " is a mutiple of 10")
else:
	print(str(num) + " isn't a multiple of 10")
