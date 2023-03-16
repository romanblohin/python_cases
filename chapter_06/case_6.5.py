rivers = {'nile': 'egypt', 'volga': 'russia', 'po': 'italy'}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}")

print("")
for river in rivers:
	print(river.title())

print("")
for country in rivers.values():
	print(country.title())