#!/usr/bin/python3

#8-9 Magicians

magician = ['bob','rob','harry']
show_magicians = []

while magician:
	na = magician.pop()
	print(na + " the magician")
	show_magicians.append(na)

print("\n")
print("name of the magicians")
for show_magician in show_magicians:
	print(show_magician)
