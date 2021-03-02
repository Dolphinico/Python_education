
# Конструкция с ключевым словом with закрывает файл после того, как надобность в нем отпадет.
with open ('text_files/pi_digit.txt') as file_object:
# Функция open() возвращает объект, представляющий файл.
# В данном случае open('pi_digits.txt') возвращает объект, представляющий файл pi_digits txt.
    contents = file_object.read()
# во второй строке программы используется метод read(), который читает все содержимое файла,
# сохраняет его содержимое в одной длинной строке в переменной contents. 
    print(contents)
# При выводе значения contents на экране появляется все содержимое файла

print('\nЧтние по строкам\n')

# бывают ситуации когда необходимо найти некую информацию в файле или собираетесь каким-то образом изменить текст.
# Для последовательной обработки каждой строки в файле можно воспользоваться
# циклом for:

file_name = 'text_files/pi_digit.txt'
with open (file_name) as file_object:
    for line in file_object:
        print(line) # добавив .rstrip(), можно удалить все пустые строки снова.

print('\nСоздание списка строк по содержимому файла\n')

# В следующем примере строки pi_digits txt сохраняются в списке в блоке with, после
# чего выводятся за пределами этого блока:

file_name = 'text_files/pi_digit.txt'
with open (file_name) as file_object:
# метод readlines() последовательно читает каждую строку из файла и сохраняет ее в списке. 
# cписок сохраняется в переменной lines, с которой можно продолжить работу после завершения блока with:
    lines = file_object.readlines()
# простом цикле for выводятся все элементы списка lines. 
# tак как каждый элемент lines соответствует ровно одной строке файла, вывод точно соответствует его содержимому.
    for line in lines:
        print(line.rstrip())

print('\nРабота с содержимым файла:\n')

# После того как файл будет прочитан в память, вы сможете обрабатывать данные
# так, как считаете нужным.

filename = 'text_files/pi_digit.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
# создается переменная pi_string для хранения цифр числа «пи»:
pi_string = ''
# далее следует цикл, который добавляет к pi_string каждую серию цифр, из которой удаляется символ новой строки:
for line in lines:
    pi_string += line.rstrip()
# здесь программа выводит строку и ее длину:
print(pi_string)
print(len(pi_string))

print('\nБольшие файлы: миллион цифр:\n')

filename = 'text_files/pi_million.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + '...') # [:52] - ограничение на вывод всего лишь 52 символов из всего файла
print(len(pi_string))

print('\nРабота с текстовым файлом, с вводом и обработкой данных:\n')

# пример такой работы, на примере поиска даты рождения в числе ПИ:

filename = 'text_files/pi_million.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
# программа запрашивает день рождения пользователя:
birthday = input("Enter your birthday, in the form ddmmyy: ")
# проверяет вхождение этой строки в pi_string:
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
