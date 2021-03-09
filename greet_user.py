import json
filename = 'username.json'

with open(filename) as f_obj:
# вызов json.load() читает информацию из файла username.json в переменную username.
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

