def build_profile(first_name, last_name, **user_info):

    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info

user = build_profile('ivan', 'ivanov', location='moscow', age=43, sex='male')

print(user)