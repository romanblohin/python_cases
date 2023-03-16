def describe_city(city, country='russia'):
	print(f"{city.title()} is in {country.title()}")

describe_city('moscow')
describe_city('tokyo', 'japan')
describe_city(country='china', city='beijing')