#!/usr/bin/python3

#6-8 Pets
petname = { 'chicken':'bob'}
petname2 = {'giffare': 'rob'} 
petname3 = { 'dinosaur':'phineas'}
petname4 = {'dog': 'ben'}

pets = [petname, petname2, petname3, petname4]

for pet in pets:
	print(pet)
print("\n")
#6-9 Favorite Places

favorite_places = {
	'bob': ['italy', 'jtaly', 'ktaly'],
	'rob': ['england', 'fngland'],
	'dob': ['france']
	}
for name, place in favorite_places.items():
	print(name + " favorite places " + str(place))
	

print("\n")
#6-10 favorite Numbers

favorite_numbers = {
	'chad': [5,2,3,4],
	'dhad': [7,3],
	'ehad': [0],
	'ghad': [1,2,3]
	}
for name, number in favorite_numbers.items():
	print(name + " favorite numbers: " + str(number))
