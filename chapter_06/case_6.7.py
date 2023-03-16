people = (
	{'first_name': 'Ivan', 'last_name': 'Ivanov', 'city': 'Moscow', 'age': 38},
	{'first_name': 'Petya', 'last_name': 'Petrov', 'city': 'Chita', 'age': 15},
	{'first_name': 'elena', 'last_name': 'kozlova', 'city': 'irkutsk', 'age': 25}
)

for user in people:
	print(f"\n{user['first_name'].title()} {user['last_name'].title()} from {user['city'].title()}")
	print(f"\tAge: {user['age']}")