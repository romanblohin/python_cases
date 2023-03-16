
def get_city_country(city, country, population=0):
	'''Функция возвращает название города и страну в отформатированном виде'''

	if population:
		formatted_string = f"{city.title()}, {country.title()} - population {population}"
	else:
		formatted_string = f"{city.title()}, {country.title()}"

	return formatted_string