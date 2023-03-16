def make_album(artist, album):

	new_album = {'artist': artist, 'album': album}
	
	return new_album

message = ""

while message != 'no':

	artist = input("Введите имя исполнителя ")
	album = input("Введите название альбома ")

	my_favorite_album = make_album(artist, album)
	print(my_favorite_album)

	message = input("Хотите продолжить ввод? ")

