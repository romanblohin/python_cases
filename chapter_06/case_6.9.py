favorite_places = {
	'olga': ['london', 'baikal', 'moscow'],
	'edward': ['london', 'moscow'],
	'mike': ['baikal']
}

for user, places in favorite_places.items():
	print(f"\n{user.title()}'s favorite places: ")
	for place in places:
		print(f"\t{place.title()}")

