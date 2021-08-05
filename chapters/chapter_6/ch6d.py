#!/usr/bin/python3

#6-11 Cities
cities = {
	'tokyo': {
		'country': 'japan',
		'population': 2000000,
		'fact': 'anime',
		},
	'delhi': {
		'country': 'india',
		'population': 4000000,
		'fact': 'cricket',
		},
	'kathmandu':{
		'country': 'nepal',
		'population': 500000,
		'fact': 'momos',
		},
	}
for city, city_info in cities.items():
	print("\nCity Name: " + city)
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']

	print("Country: country " + "\nPopulation.title(): " + str(population) + "\nFact: " + fact.title())
		
