#!/usr/bin/python3

#6-5 Rivers

rivers = {
	'nile': 'egypt',
	'mile': 'fgypt',
	'oile': 'ggypt',
	}
for river, country in rivers.items():
	print(river + " runs through " + country)

print("\n")

for river in rivers.keys():
	print(river)

print("\n")

for country in rivers.values():
	print(country)
