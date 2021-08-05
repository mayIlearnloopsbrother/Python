#!/usr/bin/python3

#8-14

def car(manufacturer, model_name, **car_info):
	profile = {}
	profile['manufacturer'] = manufacturer
	profile['model'] = model_name
	for key, value in car_info.items():
		profile[key] = value
	return profile
car_info = car('subaru', 'outback', color = 'blue', tow_package = True)
print(car_info)

car_info = car('vauxhall', 'corsa', color = 'silver', tow_package = False)
print(car_info)
