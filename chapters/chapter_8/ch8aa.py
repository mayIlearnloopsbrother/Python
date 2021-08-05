#!/usr/bin/python3

#8-13 User Profile

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

user_profile = build_profile('muhammad', 'ali', location = 'usa', field = 'boxing')
print(user_profile)

user_profile = build_profile('john', 'de vinci', location = 'italia', field = 'art')
