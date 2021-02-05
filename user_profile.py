def build_user_profile(first, last, **user_info): 
# Две звездочки перед параметром **user_info заставляют Python создать пустой словарь 
# с именем user_info и упаковать в него все полученные пары «имя—значение»
    """Строит словарь с информацией о пользователе"""
    profile = {} # создается пустой словарь с именем profile для хранения профиля пользователя.
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
# функция перебирает дополнительные пары «ключ—значение» в словаре user_info 
# и добавляет каждую пару в словарь profile.
    for key, value in user_info.items(): 
        profile[key] = value.title()
    return profile

user_profile = build_user_profile('вася', 'пупкин',
                                  location='бердянск', field='рекетир')
print(user_profile)