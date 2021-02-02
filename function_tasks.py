print('Function_tasks\n')

print('Упражнение 8-1\n')

def display_message():
    """Выводит сообщение"""
    print('Я сижу и думаю сделать бутер или нет.')

display_message()

print('\nУпражнение 8-2\n')

def favorite_book(book):
    """Выводит сообщение о любимой книге"""
    print('Одна из моих любимых книг это - ' + book.title() + '.')
favorite_book('сталкер: тени чернобыля')

print('\nУпражнение 8-3\n')

def make_shirt(size,text):
    """Выводит сообщение о размере и тексте футболки(позиционные аргументы)"""
    print('\nThe size is: ' + size + '.')
    print('Text on shirt is: ' + text)

make_shirt('M', 'Wazzap?!')

def make_shirt_2(size, text):
    """Выводит сообщение о размере и тексте футболки(именованные агрументы)"""
    print('\nThe size is: ' + size + '.')
    print('Text on shirt is: ' + text)

make_shirt_2(size='X', text='LUL')

print('\nУпражнение 8-4\n')

def make_big_shirt(size='L', text='I <3 Python'):
    """Выводит сообщение о размере и тексте футблки (аргументы по умолчанию)"""
    print('\nSize is: ' + size +'.')
    print('Text on shirt is: ' + text)
make_big_shirt()


print('\nУпражнение 8-5\n')

def describe_city(city, country):
    """Выводит сообщение о городе в стране"""
    print(city.title() + ' is in ' + country.title() + '\n')
describe_city('moscow', 'russia')

def describe_city_2(city, county = 'russia'):
    """Выводит сообщение о городе в стране"""
    print(city.title() + ' is in ' + county.title() + '.')
describe_city_2('perm')
describe_city_2('toronto','canada')
describe_city_2('omsk')

print('\nУпражнение 8-6\n')

def city_country_3(city, country):
    """Выводит сообщение пару город-страна"""
    pare = city + ', ' + country
    return pare.title()
full_pare = city_country_3('perm','russia')
print(full_pare)
full_pare = city_country_3('omsk','russia')
print(full_pare)
full_pare = city_country_3('tomsk','russia')
print(full_pare)

print('\nУпражнение 8-7\n')

def make_album(artist_name, album_name, song_list=''):
    """Возвращает словарь с информацие о музыкальном альбоме"""
    album={'artist': artist_name, 'album': album_name}
    if song_list:
        album['song_list']= song_list
    return album

album_inf = make_album('attlas', 'out here with you', song_list= 14)
print(album_inf)
album_inf = make_album('no mana', 'secert level', song_list= 5)
print(album_inf)
album_inf = make_album('EDDIE', 'blueprints', song_list= 16)
print(album_inf)

print('\nУпражнение 8-8\n')

def make_album_2(artist_name, album_name):
    """Возвращает словарь с информацие о музыкальном альбоме"""
    album = artist_name + ' - ' + album_name
    return album.title()
while True:
    print('\nPlease enter the artist name and album name')
    print("(enter 'q' if u wanna exit)")
    ar_name = input('Artist name: ')
    if ar_name == 'q':
        break
    al_name = input('Album name: ')
    if al_name == 'q':
        break
    maked_album = make_album_2(ar_name, al_name)
    print('\nThis album by ' + maked_album + ' is awesome!')

print('\nУпражнение 8-9\n')

def show_magicians_1(magician):
    """Выводит имя каждого фокусника в списке"""
    for mag in magician:
        message = ('Hello new one ' + mag.title() +'!')
        print(message)

magicians = ['boba','biba','joka', 'boka']
show_magicians_1(magicians)

print('\nУпражнение 8-10\n')

def show_magicians_2(magician):
    """Выводит имя каждого фокусника в списке"""
    for mag in magician:
        message = ('Hello new one ' + mag.title() +'!')
        print(message)

def make_great(magician):
    """Добавляет к волшебникам Great"""
    for mag in magician:
        mag = "Great " + magicians.pop(0)
        magician.append(mag)
        print(mag.title())

magicians = ['boba','biba','joka', 'boka']

show_magicians_2(magicians)
make_great(magicians)

print('\nУпражнение 8-11\n')

def show_magicians_3(magician):
    """Выводит имя каждого фокусника в списке"""
    for mag in magician:
        message = ('Hello new one ' + mag.title() +'!')
        print(message)

def make_great_1(magician):
    """Добавляет к волшебникам Great"""
    for mag in magician:
        mag = "Great " + magicians.pop()
        new_magicians.append(mag)
        print(mag.title())

magicians = ['boba','biba','joka', 'boka']
new_magicians = []

show_magicians_3(magicians)
make_great_1(magicians[:]) # копия списка magicians 
show_magicians_3(new_magicians) # проверка на то, что есть и старый список и копия

print('\nУпражнение 8-12\n')

# 8-12 Сэндвичи: напишите функцию, которая получает список компонентов сэндвича 
# Функция должна иметь один параметр для любого количества значений, переданных при вызове
# функции, и выводить описание заказанного сэндвича Вызовите функцию три раза с разными количествами аргументов

def making_sandwich_1(*components):
    """Выводит список компонентов в сендвиче"""
    print(components)

making_sandwich_1('meat')
making_sandwich_1('meat', 'salad')
making_sandwich_1('meat', 'salad','tomato')

def making_sandwich(*components):
    """Выводит список компонентов в сендвиче"""
    print('\nYour sandwich consis of: ')
    for component in components:
        print(component)

making_sandwich('meat')
making_sandwich('meat', 'salad')
making_sandwich('meat', 'salad','tomato')

print('\nУпражнение 8-13\n')
# 8-13 Профиль: начните с копии программы user_profile.py Создайте собственный профиль
# вызовом build_profile(), укажите имя, фамилию и три другие пары «ключ—значение» для вашего описания

def user_accaunt(first, last, **user_info): 
    """Строит словарь с информацией о пользователе"""
    profile = {} 
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): 
        profile[key] = value
    return profile
user_profile = user_accaunt('coffe', 'brazil', kind = 'latte', price='5$')
print(user_profile)

print('\nУпражнение 8-14\n')

# 8-14 Автомобили: напишите функцию для сохранения информации об автомобиле в словаре 
# Функция всегда должна возвращать производителя и название модели, но при этом она
# может получать произвольное количество именованных аргументов
# Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация)
# Ваша функция должна работать для вызовов следующего вида:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)

# Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена правильно

def car_info(producer, model, **other_info):
    """Сохранение и вывод информации об автомобиле"""
    spec = {}
    spec['brand'] = producer
    spec['model'] = model
    for key, value in other_info.items():
        spec[key] = value
    return spec
car_spec = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car_spec)