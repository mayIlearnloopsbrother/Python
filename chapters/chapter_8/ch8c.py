#!/usr/bin/python3

#8-8 User Albums

def make_album(artist, album):
	alb = artist + ' , ' + album
	return alb.title()

while True:
	print("'q' to quit.. Music ")

	a_artist = input("artist: ")
	if a_artist == 'q':
		break
	
	b_album = input("album: ")
	if b_album == 'q':
		break
	
	a = make_album(a_artist, b_album)
	print("You listen to: , " + a + "\n")

