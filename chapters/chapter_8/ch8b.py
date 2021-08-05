#!/usr/bin/python3

#8-6 City Names

def city_country(city_name, country_name):
	a = city_name + ' , ' + country_name
	return a.title()
print("city name and countries")

b = city_country('Santiago', 'Chile')
print(b)

b = city_country('Kathmandu', 'Nepal')
print(b)

b= city_country('Delhi', 'India')
print(b)

print("\n")

#8-7 Album
def make_album(artist_name, album_title, tracks=''):
	if tracks:
		alb = artist_name + ' ' + album_title + ' ' + str(tracks)
	else:
		alb = artist_name + ' ' + album_title
	return alb.title()
print("artist name and their ablum")

re = make_album('grease', 'slipknot', tracks=12)
print(re)

re = make_album('reese', 'metallica', tracks=8)
print(re)

re = make_album('sav', 'chicken nuggets')
print(re)
