print('\nФункции  в Python:')

print('\nОпределение функции def:')


def greet_user_1():  # -------------------------}
    """Выводит простое приветствие."""  # -------} определение функции, что она будет делать
    print('Hello!')  # -------------------------}


greet_user_1()  # - вызов функции

print('\nПередача информации функции:\n')


def greet_user_2(username):
    """Выводит простое приветствие."""
    print('Hello ' + username.title() + '!')


greet_user_2('Даниил')

print('\nПередача аргументов: Позиционные агрументы:')
# Определение функции может иметь несколько параметров, и может оказаться, что
# при вызове функции должны передаваться несколько аргументов


def discribe_pets_1(animal_type, pet_name):
    """Выводит информацию о животном"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name.title() + '.')


# Функция может вызываться в программе столько раз, сколько потребуется
discribe_pets_1('dog', 'dogg')

# Функция может иметь любое количество позиционных аргументов. При вызове
# функции Python перебирает аргументы, приведенные в вызове, и сопоставляет
# каждый аргумент с соответствующим параметром из определения функции.

print('\nИменованные аргументы:\n')


def describe_pet_2(animal_type, pet_name):
    """Выводит сообщение о животном"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name.title() + '.')


describe_pet_2(animal_type='dog', pet_name='dogg')

# Функция не меняется, но в этот раз python 100% понимает что animal_type это dog, а pet_name это dogg
# В данном случае порядок следования аргументов не важен, тк они уже определены

print('\nЗначения по умолчанию:\n')

# в этом примере по умолчанию задается параметр animal_type = 'dog',
# python будет знать что по умолчанию стоит в этом параметре и теперь его не нужно прописывать еще раз при вызове функции


def describe_pet_3(pet_name, animal_type='dog'):
    """Выводит сообщение о животном"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name.title() + '.')


# что бы вывести имя любого другого животного, функция будет вызываться так:
describe_pet_3(pet_name='dogg')
# describe_pet_3(animal_type='cat', pet_name='catt')

print('\nВозвращаемое значение:\n')

# Функция не обязана выводить результаты своей работы. Вместо этого она может
# обработать данные, а затем вернуть значение или набор сообщений.

# Команда return передает значение из функции в строку, в которой эта функция была вызвана.


def get_formatted_name_1(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_1('jimmy', 'hendrix')
print(musician)

# Вызывая функцию, которая возвращает значение, необходимо предоставить пере-
# менную, в которой должно храниться возвращаемое значение. В данном случае
# возвращаемое значение сохраняется в переменной musician

print('\nНеобязательные аргументы:\n')

# Иногда бывает удобно сделать аргумент необязательным, чтобы разработчик,
# использующий функцию, мог передать дополнительную информацию только в том
# случае, если он этого захочет. Чтобы сделать аргумент необязательным, можно
# воспользоваться значением по умолчанию.

# прмер такого кода:


def get_formatted_name_2(first_name, middle_name, last_name):
    """Возвращает аккуратно отформатированное имя"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_2('jhon', 'lee', 'hooker')
print(musician)

# но вторые имена нужны не всегда, в таком случае необходим следущий прием:


def get_formatted_name_3(first_name, last_name, middle_name=''):
    """Возвращает аккуратно отформатированное имя"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_3('jimi', 'hendrix')
print(musician)
musician = get_formatted_name_3('jhon', 'hooker', 'lee')
print(musician)

# если соблюдается первое условие в if, то функция будет выводить 3 значения, если при возврате в full_name
# условие не соблюдается, то  функция выводит 2 значения

print('\nВозвращение словаря\n')

# Функция может вернуть любое значение, нужное вам, в том числе и более сложную
# структуру данных (например, список или словарь).


def build_person_1(first_name, last_name):
    """Возвращает словарь с информацией о человеке"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person_1('jimi', 'hendrix')
print(musician)

# в данном примере указано как можно добавить новую информацию в словарь:


def build_person_2(first_name, last_name, age=''):
    """Возвращает словарь с информацией о человеке"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person_2('jimi', 'hendrix', age=24)
print(musician)

# В определение функции добавляется новый необязательный параметр age, кото-
# рому назначается пустое значение по умолчанию. Если вызов функции включает
# значение этого параметра, то значение сохраняется в словаре. Функция всегда
# сохраняет имя, но ее также можно модифицировать, чтобы она сохраняла любую
# необходимую информацию о человеке.

print('\nИспользование функции в цикле while\n')


def get_formatted_name_4(first_name, last_name):
    """Возвращает аккуратно отформатированное имя"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# здесь вступает цикл while + input


while True:
    print('\nPlease tell me your name:')
# что бы цикл не был бесконечным, нужно дать пользователю возможность завершить программу - break:
    print("(enter 'q' at any time to quit)")
    f_name = input('Frist name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name_4(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')

print('\nПередача списка\n')

# Часто при вызове функции удобно передать список — имен, чисел или более
# сложных объектов (например, словарей). При передаче списка функция получает
# прямой доступ ко всему его содержимому.

# пример на программе, приветствующая всех людей из списка:


def greet_users_1(names):
    """Вывод простого сообщения для каждого пользователя в списке"""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)


usernames = ['sanya', 'daniil', 'artem', 'roma']
greet_users_1(usernames)

print('\nИзменение списка в функции\n')

# Если вы передаете список функции, код функции сможет изменить список. Все
# изменения, внесенные в список в теле функции, закрепляются, что позволяет эф-
# фективно работать со списком даже при больших объемах данных.

# пример реализации кода без использования функции, только цикл while,
# на примере компании котороая печатает на 3D принтере:

# сначала мы создаем список деталей(которые принес заказсчик):
unprinted_designs = ['iphone case', 'robot servant', 'little doll', 'mini car']
complited_models = []

# цикл while последовательно печатает каждую модель до конца списка.
# после печати каждая модель будет перемещена в новый список complited_models

while unprinted_designs:
    current_design = unprinted_designs.pop()
    # далее идет команда печати моделей:
    print('Printing model: ' + current_design)
    complited_models.append(current_design)

# а затем выводим список уже готовых деталей:
print("\nThe following models have been printed:")
for model in complited_models:
    print(model)

print('\nВерсия когда с использованием функции\n')
# теперь, меняем код в сторону функциональности, добавляем 2 функции, каждая будет решать свою задачу:


def print_models(unprinted_designs, complited_models):
    # сначала определяется функция print_models() с двумя параметрами: список
    # моделей для печати и список готовых моделей. Функция имитирует печать каж-
    # дой модели, последовательно извлекая модели из первого списка и перемещая
    # их во второй список.
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # имитация печати модели на 3D принтере:
        print('Printing model: ' + current_design)
        complited_models.append(current_design)


def show_complited_models(complited_models):
    # здесь определяется функция show_completed_models()
    # с одним параметром: списком напечатанных моделей. Функция show_completed_
    # models() получает этот список и выводит имена всех напечатанных моделей.
    """Выводит информацию о всех напечатаных моделях"""
    print('\nThe follofing models have been printed:')
    for complited_model in complited_models:
        print(complited_model)

# сама программа:


unprinted_designs = ['iphone case', 'robot servant', 'little doll', 'mini car']
complited_models = []

print_models(unprinted_designs[:], complited_models)
show_complited_models(complited_models)


print('\nЗапрет изменения списка в функции\n')

# Иногда требуется предотвратить изменение списка в функции.
# допустим после печати всех моделей исходный список нужно оставить для отчетности.
# Но, поскольку все имена моделей были перенесены из списка unprinted_designs, остался только
# пустой список; исходная версия списка потеряна.

# в таком случае, нужно передать функцию копии оригинального списка,
# тогда все изменения будут применяться на копию, оригинал останется неизменным

# Чтобы передать функции копию списка, можно поступить так:
# имя_функции(имя_списка[:])

# Если удаление элементов из списка unprinted_designs в print_models py нежелательно, функцию
# print_models() можно вызвать так:

print_models(unprinted_designs[:], complited_models)


print('\nПередача произвольного набора аргументов:\n')

# в ситуации когда вы не знаете заранее, сколько аргументов должно быть передано функции, следует применить такой код:


def making_pizza(*toppings):
    # функция получает один параметр - *toppings, он объеденит все аргументы, заданные в командной строке
    """Вывод списка заказанных дополнений"""
    print(toppings)


making_pizza('pepperoni')
making_pizza('mushrooms', 'potato', 'beef')
# символ * в данном случае упаковывает все полученные значения при вызове функции,
#  при этом topping становится кортежем, если поместить только 1 значение

# Теперь команду print можно заменить циклом, который перебирает список
# дополнений и выводит описание заказанной пиццы:


def making_pizza_2(*toppings):
    """Вывод списка заказанных дополнений"""
    print('\nMaking pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


making_pizza_2('pepperoni')
making_pizza_2('mushrooms', 'potato', 'beef')

# Этот синтаксис работает независимо от количества аргументов, переданных функции.

print('\nПозиционные аргументы с произвольными наборами аргументов:')

# если в ситуации необходимо вызвать функцию с разным количеством аргументов, его параметр должен стоять в конце:


def making_pizza_3(size, *toppings):
    """Выводит описание пиццы"""
    print('\nMaking a ' + str(size) +
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


# в определении функции питон сохраняет первое полученное значение в параметре size
# остальное сохраняется в кортеже *toppings
making_pizza_3(12, 'banana')
making_pizza_3(23, 'olive', 'apple', 'cheese')

print('\nИспользование произвольного набора именованных аргументов:\n')

# Иногда программа должна получать произвольное количество аргументов,
# но заранее не известно, какая информация будет передаваться функции.

# Один из возможных примеров — построение пользовательских профилей,
# вы знаете, что вы получите информацию о пользователе, но не знаете заранее, какую именно:


def build_user_profile(first, last, **user_info): 
# Две звездочки перед параметром **user_info заставляют Python создать пустой словарь 
# с именем user_info и упаковать в него все полученные пары «имя—значение»
    """Строит словарь с информацией о пользователе"""
    profile = {} # создается пустой словарь с именем profile для хранения профиля пользователя.
    profile['first_name'] = first
    profile['last_name'] = last
# функция перебирает дополнительные пары «ключ—значение» в словаре user_info 
# и добавляет каждую пару в словарь profile.
    for key, value in user_info.items(): 
        profile[key] = value
    return profile

user_profile = build_user_profile('albert', 'einstein',
                                  location='princeton', field='physics')
print(user_profile)


print('\nХранение функций в модулях, импортирование всего модуля:\n')