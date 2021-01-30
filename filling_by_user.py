print('\nЗаполнение словаря данными, введенными пользователем\n')
# При каждом проходе цикла while, программа запрашивает необходимое количество данных,
# все данные будут сохранятся в словаре
# пример работы подобной программы, в виде опросника:

responses = {}
# Установка флага продолжения опроса.
polling_active = True

while  polling_active:
# Запрос имени и ответа пользователя.
    name = input('\nWhat is your name? ')
    response = input('\nWhich city would you like to visit? ')
    
# Ответ сохраняется в словаре:
    responses[name] = response
# Проверка продолжения опроса.
    repeat = input('Would you like to let another person respond? (yes / no) ')
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты.
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would  like to visit ' + response + '.')