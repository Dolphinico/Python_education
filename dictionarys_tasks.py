#Упражнения по словарям 6-1-3
print('Упражнение 6-1\n')

myself = {'age': 25, 'first_name': 'Daniil', 'last_name': 'Leontev', 'city': 'Perm'}

print('My name is ' + myself['first_name'] + ' ' + myself['last_name'] + ',' + '\ni am ' 
    + str(myself['age']) + ' years old' + ' and i live in ' + myself['city'] +'.')

print('\nУпражнение 6-2\n')

favorite_digits = {
    'daniil': 7,
    'sanya': 14,
    'artem': 87,
    'roma': 4,
    'andrey': 13,
}
for digit in favorite_digits:
    print(digit.title() + ' favorite number is ' + str(favorite_digits[digit])) 
    #цикл for для перебора списка пар в словаре favotie_digits

print('\nУпражнение 6-3\n')

glossary = {
    'оператор': ' - это символ, который выполняет операцию над одним или несколькими операндами',
    'операнд': ' - операндом выступает переменная или значение, над которыми проводится операция',
    'метод': ' - метод связан с конкретным объектом списка и знает, что именно его он должен модифицировать',
    'переменная': ' - обозначенная область памяти, содержащая какое-то значение',
    'конкатенация': ' - означает соединение или добавление двух объектов вместе',
}

for info in glossary:
    print(info.title() + glossary[info] + '.')

print('\nУпражнение 6-4\n')

#изменение глоссария с учтом проеденного материала:

glossary = {
    'оператор': ' - это символ, который выполняет операцию над одним или несколькими операндами',
    'операнд': ' - операндом выступает переменная или значение, над которыми проводится операция',
    'метод': ' - метод связан с конкретным объектом списка и знает, что именно его он должен модифицировать',
    'переменная': ' - обозначенная область памяти, содержащая какое-то значение',
    'конкатенация': ' - означает соединение или добавление двух объектов вместе',
    'словарь': ' - набор пар ключ-значение, помогающее держать информацию об одном или нескольих объектах',
    'python': ' - замечательный и интересный язык программирования',
    'pep8': ' - этот документ описывает соглашение о том, как писать код для языка python, включая стандартную библиотеку, входящую в состав python',
    '.keys()': ' - метод для определения ключа в паре ключ-значение',
    '.values()': ' - метод для определения значения в паре ключ-значение',
}
for info in glossary:
    print(info.title() + glossary[info] + '.')

print('\nУпражнение 6-5\n')

river_party = {
    'nile': 'egypt',
    'volga': 'volgograd',
    'kama': 'perm',
}

for river in river_party.keys():
    print('The ' + river.title() + ' runs through ' + river_party[river].title())

river_party = {
    'nile': 'egypt',
    'volga': 'volgograd',
    'kama': 'perm',
}

for river in river_party.keys():
    print(river.title())

river_party = {
    'nile': 'egypt',
    'volga': 'volgograd',
    'kama': 'perm',
}

for city in river_party.values():
    print(city.title())

print('\nУпражнение 6-6\n')

favorite_languages = {
'jentema': 'c',
'shelkote': 'c#',
'edward': 'ruby',
'sanya': 'paskal',
'daniil': 'python',

}
not_polled = ['artem','maksim']
for ppl in favorite_languages.keys():
    print(ppl.title() + ', thank you for participating in poll!')
for out in not_polled:
     print(out.title() + ' , please take a poll!')

#упражнение 6-7
print('\nУпражниение 6-7\n')

people =  {
    'user_1': {
        'first': 'daniil',
        'second': 'leontev',
        'age': '25',
        'location': 'perm',
    },
    'user_2': {
        'first': 'sanya',
        'second': 'sokolov',
        'age': '24',
        'location': 'perm',
    },
    'user_3': {
        'first': 'zero',
        'second': 'two',
        'age': '26',
        'location': 'japan',
    },
}
for username, userinfo in people.items():
    print('\nUsers: ' + username)
    full_info = userinfo['first'] + ' ' + userinfo['second']
    age = userinfo['age']
    location = userinfo['location']
    print('\tFullname: ' + full_info.title())
    print('\tAge: ' + str(age))
    print('\tLocation: ' + location.title())

#Упражнение 6-8
print('\nУпражнение 6-8\n')

pets = {
    'timon': {
        'pet': 'cat',
        'petholder_first': 'sanya',
        'petholder_last': 'sokolov',
    },
    'kotya': {
        'pet': 'cat',
        'petholder_first': 'fedya',
        'petholder_last': 'tiran',
    },
    'doggo': {
        'pet': 'dog',
        'petholder_first': 'robn',
        'petholder_last': 'bobn',
    },
}
for petname, petinfo in pets.items():
    print('\nPetname: ' + petname.title())
    pet_holder = petinfo['petholder_first'] + ' ' + petinfo['petholder_last']
    kind = petinfo['pet']
    print('\tPet holder: ' + pet_holder.title())
    print('\tKind: ' + kind.title())

#упражниене 6-9
print('\nУпражнение 6-9\n')

favorite_places = {
    'user_1': {
        'first': 'daniil',
        'last': 'leontev',
        'places': 'japan, uk',
    },
    'user_2': {
        'first': 'daniil',
        'last': 'leontev',
        'places': 'usa, netherlands',
    },

    'user_3': {
        'first': 'daniil',
        'last': 'leontev',
        'places': 'canada'
    },
}
for users, userinfo  in favorite_places.items():
    print('\nUser name: ' + users)
    info = userinfo['first'] + ' ' + userinfo['last']
    place = userinfo['places']
    print('\tFriend: ' + info.title())
    print('\tHis favorite place is: ' + place.title())
    
#Упражнение 6-10
print('\nУпражнение 6-10\n')

favorite_digits = {
    'daniil':{
        'fav_digits': '7,19,14',
    },
    'sanya': {
        'fav_digits': '14,15,21',
    },
    'artem':{
        'fav_digits': '87,44,555,666',
    },
    'roma': {
        'fav_digits': '4,23,11',
    },
    'andrey': {
        'fav_digits': '13,12312,22,33,44',
    },
}
for name, digits in favorite_digits.items():
    print('\nFriend name: ' + name.title())
    fav_digits = digits['fav_digits']
    print('\tFavorite numbers are: ' + str(fav_digits))

#Упражнение 6-11
print('\nУпражнение 6-11\n')

cities = {
    'toronto': {
        'country': 'canada',
        'population': '2 731 571 чел.',
        'fact': 'здесь живет Deadmau5',
    },
    'moscow': {
        'country': 'russia',
        'population': '11,92 миллиона',
        'fact': 'москва не резиновая',
    },
    'sydney': {
        'country': 'australia',
        'population': '5,312 миллиона',
        'fact': 'здесь проводились все The International по Dota 2',
    },
}
for cityname, cityinfo in cities.items():
    print('\nCity name: ' + cityname.title())
    country = cityinfo['country']
    population = cityinfo['population']
    fact = cityinfo['fact']
    print('\tThe country of this city is ' + country.title())
    print('\tPopulation of this city is about ' + population)
    print('\tInteresting fact that ' + fact)