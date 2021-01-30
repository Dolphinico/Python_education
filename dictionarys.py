#Словари в Python
print('Словари в Python, простой словарь\n')

alien_0 = {'color': 'green', 'points': 5} #в словаре содержится 2 атрибута, цвет(color) и очки(points),
#следующие две команды print считывают информацию со словаря и выводят ее
print(alien_0['color'])
print(alien_0['points'])

#Работа со словарями
print('\nРабота со словарями\n') #словарь в Python это ключ-значение (points-ключ 5- значение)

new_points = alien_0['points'] #определяем словарь, в данном случае это alien_0 в котором есть 2 ключ-значения
#color и points, на этом примере выводятся points'ы
print('You just earned ' + str(new_points) + ' points!\n')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
#добавление новых значний в словарь, это можно делать в любое время, 
#по итогу в alien_0 добавятся 2 новых пары ключ-значение
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)
#создание пустого словаря
print('\nCоздание пустого словаря\n')
#в данном слуаче программа начинает с пустого словаря, а затем начинает добавлять в него новые данные
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
#изменение значений в словаре
print('\nизменение значений в словаре\n')

alien_0 = {'color': 'green'} #изначальный цвет - зеленый, при выполнении программы выводится соответствующее сообщение
print("The alien is " + alien_0['color'] + ".") 

alien_0['color'] = 'yellow' #здесь мы меняем значение, в паре ключ-значение на новый цвет yellow
print('The alien is now ' + alien_0['color'] + '.')

#отслеживание передвижения объекта
print('\nOтслеживание передвижения объекта\n')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))
#В данном примере пришелец перемещяется вправо
#теперь определим величину смещения на основании текущей скорости
if alien_0['speed'] == 'slow':
    x_incresment = 1
elif alien_0['speed'] == 'medium':
    x_incresment = 2
else:
    x_incresment = 3 #пришелец двигается быстро
#новая позиция пришельца равна сумме старой позиции и наращивания:
alien_0['x_position'] = alien_0['x_position'] + x_incresment
print('New position: ' + str(alien_0['x_position']))

#удаление пары ключ-значение
print('\nУдаление пары ключ-значение\n')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] #в этом примере удаляется пара points - 5, отменить удаление уже нельзя
print(alien_0)

#Словарь с однотипными объектами, например может использоваться для хранения одного вида информации об одном объекте
print('\nСловарь с однотипными объектами\n')

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + 
    favorite_language['sarah'].title() + 
    '.')

#Перебор словаря, перебор всех пар "ключ-значение"
print('\nПеребор словаря, перебор всех пар "ключ-значение"')

user_0 = {
    'username': 'dolphin',
    'fisrt': 'daniil',
    'second': 'leontev',

}
#вариант перебора через цикл for:

for key, value in user_0.items(): #.items() возвращает список пар ключ-значение, цикл for сохраняет компоненты пары в указанных переменных (key,value)
    print('\nKey: ' + key)
    print('Value: ' + value)

#key,value - переменные могут быть любыми, но главное что бы они подходили по смыслу к списку и легко читались/понимались

#Перебор всех слов в словаре
print('\nПеребор всех слов в словаре\n')

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
#метод keys() удобен когда не планируется работать со всеми значениями в словаре
for name in favorite_languages.keys(): #Используйте явный вызов метода keys(), если вы считаете, что он упростит чтение
#вашего кода, — или опустите его при желании, так как конкретно в этом примере или необходимости вызвать только "ключи", 
#можно использовать обычный цикл for name in favorite_languages:
    print(name.title())

#вывод "ключа" через цикл for:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil','sarah']
for name in favorite_languages.keys(): #обычный вывод "ключей" через цикл for
    print(name.title())
    if name in friends: # проверка условия если "ключ" в новом списке, то выводится специальное сообщение
        print(' Hi ' + name.title() + 
        ', I see your favorite language is '
         + favorite_languages[name].title() + '!')

#также метод keys() можно применять для определения отсутствия "ключа" в словаре:

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
} 

if 'erin' not in favorite_languages.keys(): #при помощи оператора not мы определяем что если переменная 'erin', не в списке,
#выполняется команда вывода определенного сообщения.
    print("Erin, please take our poll!")

#Упорядоченный перебор ключей словаря функцией sorted()

print('\nУпорядоченный перебор ключей словаря функцией sorted()\n')

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in sorted(favorite_languages.keys()): #перед тем как выполнится цикл for, python отдает команду сначала отсортировать список, 
#а затем перебрать его и вывести требуемеое сообщение
    print(name.title() + ', thank you for taking the poll.')

#Перебор всех "значений" в словаре .values()
print('\nПеребор всех "значений" в словаре .values()\n')

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
#в конекретном примере мы перебираем циклом for все "значения" из пары "ключ-значение" при помощи метода .values()
print('The following language have been mentioned: ')
for language in favorite_languages.values(): 
    print(language.title())
#в текущем примере "значения" извлекаются из словаря без проверки на возможные повторения, 
#но воспользовавшись множеством set(), можно получить список значений без повторений, 
#это делаете в том случае, если в списке будет много одинаковых значений:

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print('The following language have been mentioned: ')
for language in set(favorite_languages.values()): #в результате из 4 пунктов в списке, выводится 3, тк Python есть в списке дважды
    print(language.title())

#Вложение(список словарей)
print('\nВложение(список словарей)\n')

#пример на пришельцах(дубль в файле aliens.py)

alien_0 = {'color': 'green', 'points': '5' }
alien_1 = {'color': 'yellow','points': '10' }
alien_2 = {'color': 'red', 'points': '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#создание "флота" при помощи метода range()
print('\nсоздание "флота" при помощи метода range()\n')
#сначала создается пустой список:
aliens = []
#создание флота из 30 пришельцев:
for alien_number in range(0,30): #<- функция range() указывает python сколько раз цикл должен повториться,
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #при каждом повторе создается именно этот пришеле(либо другой указанный)
    aliens.append(new_alien)
#Например, чтобы превратить первых трех пришельцев в желтых,
#двигающихся со средней скоростью и приносящих игроку по 10 очков, либо в быстрых по 15 очков можно
#действовать так:
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

#вывод первых 5 пришельцев при помощи среза (slice):
for alien in aliens[0:5]:
    print(alien)
print('...')
#вывод точного количества созданных пришельцев:
print('Total number of aliens: ' + str(len(aliens)))
#Все пришельцы обладают одинаковыми характеристиками, но Python рассматри-
#вает каждого пришельца как отдельный объект, что позволяет изменять атрибуты
#каждого владельца по отдельности.

print('\nСписки в словаре:\n')

#можно помещать список в словарь и работать с ним например так:
#сохраниение информации о заказе:
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#описание заказа: 
print('You ordered a ' + pizza['crust']+ ' - crust pizza ' 
+ 'with following toppings: ')
for topping in pizza['toppings']:
    print('\t' + topping)

#Вложение списка в словарь может применяться каждый раз, когда с одним ключом
#словаря должно быть связано более одного значения 

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'], 
'phil': ['python', 'haskell'],
} 
#В цикле for словаря создается другой цикл для перебора
#списка языков, связанных с каждым участником:
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name.title() + "'s favorite language is: ")
    else:
        print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())

#Словарь в словаре на примере словаря пользователей
print('\nСловарь в словаре на примере словаря пользователей\n')

users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location'] 
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())