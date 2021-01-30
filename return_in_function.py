print('Возвращаемое значение:\n')

# Функция не обязана выводить результаты своей работы. Вместо этого она может
# обработать данные, а затем вернуть значение или набор сообщений.

# Команда return передает значение из функции в строку, в которой эта функция была вызвана.

def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimmy', 'hendrix')
print(musician)

# Вызывая функцию, которая возвращает значение, необходимо предоставить пере-
# менную, в которой должно храниться возвращаемое значение. В данном случае
# возвращаемое значение сохраняется в переменной musician

print('\nНеобязательные аргументы:\n')

# Иногда бывает удобно сделать аргумент необязательным, чтобы разработчик, 
# использующий функцию, мог передать дополнительную информацию только в том
# случае, если он этого захочет. Чтобы сделать аргумент необязательным, можно
# воспользоваться значением по умолчанию.

#прмер такого кода:

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
musician = get_formatted_name_3('jhon', 'hooker','lee')
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

def build_person_2(first_name, last_name, age =''):
    """Возвращает словарь с информацией о человеке"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person_2('jimi', 'hendrix', age = 24)
print(musician)

# В определение функции добавляется новый необязательный параметр age, кото-
# рому назначается пустое значение по умолчанию. Если вызов функции включает
# значение этого параметра, то значение сохраняется в словаре. Функция всегда
# сохраняет имя, но ее также можно модифицировать, чтобы она сохраняла любую
# необходимую информацию о человеке.

