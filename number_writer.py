# Напишем короткую программу для сохранения набора чисел и другую программу,
# которая будет читать эти числа обратно в память.
# Первая программа использует функцию json.dump(), а вторая — функцию json.load().

# Функция json.dump() получает два аргумента: сохраняемые данные и объект файла, используемый для сохранения.

# В следующем примере json.dump() используется для сохранения списка чисел:


import json
# Программа импортирует модуль json и создает список чисел для работы
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
# файл открывается в режиме записи, чтобы модуль json мог записать в него данные:
with open(filename, 'w') as f_obj:
# функция json.dump() используется для сохранения списка numbers в файле numbers json:
    json.dump(numbers, f_obj)