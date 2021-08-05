#!/usr/bin/python3

#6-1 Person
person = {'first_name': 'Sangram', 'last_name': 'Limbu', 'age': 49, 'city': 'Basingstoke'}

print("\nhi mr " + person['first_name'] + " " + person['last_name'])
print("are you " + str(person['age']) + " years old?")
print("do you live at " + person['city'] + "?")

#6-2 Favorite Numbers
print("\n")
people_nos = {
	'jane' : 32,
	'bart' : 22,
	'mark' : 28,
	'hart' : 30,
	}
print("Jane's fav number " + str(people_nos['jane']))
print("Bart's fav number " + str(people_nos['bart']))
print("Mark's fav number " + str(people_nos['mark']))
print("Hart's fav number " + str(people_nos['hart']))
