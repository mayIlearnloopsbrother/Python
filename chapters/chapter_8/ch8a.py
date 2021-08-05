#!/usr/bin/python3

#8-3/4 T-Shirt

def make_shirt( text, size='L'):
	print("size: " + size + "\nyour text: " + text + "\n")
make_shirt('I love Python')
make_shirt('default message', size='M')



#8-5 Cities

def describe_city(city, country='UK'):
	print(city + " is in " + country)
describe_city('glasgow')
describe_city('hlasgow')
describe_city('ilasgow')
describe_city('delhi', country='India')
