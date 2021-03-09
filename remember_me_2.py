# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

# Пример рефаторинга:

# Основной задачей remember_me_2.py является вывод приветствия для пользователя,
# поэтому весь существующий код будет перемещен в функцию greet_user()

import json
def get_stored_username(): 
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
# Если файл username json не существует,то функция возвращает None, если существует, выводит username
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'    
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_user ():
    """Приветствует пользователя по имени"""
    username = get_stored_username()
# программа выводит приветствие для пользователя,
# если попытка получения имени пользователя была успешной;
# в противном случае программа запрашивает новое имя пользователя:
    if username:
        print("Welcome back, " + username +"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

        
greet_user()


