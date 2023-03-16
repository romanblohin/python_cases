def city_country(city, country):
	message = f"{city}, {country}"
	return message.title()

formatted_info = city_country('moscow', 'russia')
print(formatted_info)
formatted_info = city_country('tokyo', 'japan')
print(formatted_info)
formatted_info = city_country('beijing', 'china')
print(formatted_info)