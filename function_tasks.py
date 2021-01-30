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
