favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

new_users = ['phil', 'olga', 'sarah', 'anton']

for user in new_users:
    if user in favorite_languages:
        print(f"{user.title()} спасибо что прошли опрос")
    else:
        print(f"{user.title()} предлагаю пройти опрос")
