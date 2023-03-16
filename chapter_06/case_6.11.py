cities = {
	'moscow': {
	'country': 'russia',
	'population': 13_097_539 ,
	'fact': 'cамый крупный город Европы по площади'
	},
	'tokyo': {
	'country': 'japan',
	'population': 14_043_239,
	'fact': 'являясь одним из самых больших городов на Земле, \n\tсчитается самым безопасным городом в мире'
	},
	'london': {
	'country': 'great britain',
	'population': 8_961_989,
	'fact': 'c 1825 по 1925 год был крупнейшим городом мира'
	}
}

for city, info in cities.items():
	print(f"\n{city}:")
	print(f"\tCountry: {info['country'].title()}")
	print(f"\tPopulation: {info['population']}")
	print(f"\tFact: {info['fact']}")
	
