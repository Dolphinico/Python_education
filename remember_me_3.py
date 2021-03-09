# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

import json

filename = 'username.json'
try:
# программа пытается открыть файл username json:
    with open(filename) as f_obj:
# Если файл существует, программа читает имя пользователя в память
# и выводит сообщение, приветствующее пользователя, в блоке else:
        username = json.load(f_obj)
# Если программа запускается впервые, то файл username json не существует,
# и происходит исключение FileNotFoundError:
except FileNotFoundError:
# в таком случае Python переходит к блоку except, в котором пользователю предлагается ввести имя:
    username = input("What is your name? ")
# Затем программа вызывает json.dump() для сохранения имени пользователя и выводит приветствие:
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username +"!")