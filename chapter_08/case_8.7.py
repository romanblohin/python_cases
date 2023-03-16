def make_album(artist, album, tracks=None):

	new_album = {'artist': artist, 'album': album}
	
	if tracks:
		new_album['tracks'] = tracks

	return new_album


album_1 = make_album('nirvana', 'in utero', tracks=12)
print(album_1)
album_1 = make_album('rammstein', 'mutter')
print(album_1)
album_1 = make_album('the prodigy', 'the fat of the land', 10)
print(album_1)