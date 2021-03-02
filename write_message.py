filename = 'programming.txt'
# Первый аргумент, как и прежде, содержит имя открываемого файла. Второй аргумент 'w' сообщает
# Python, что файл должен быть открыт в режиме записи.
with open (filename, 'w') as file_object:
# метод write() используется с объектом файла для записи строки в файл.
# Программа не выводит данные на терминал, но, открыв файл programming txt, вы
# увидите в нем одну строку, с текстом который был указан:
    file_object.write('I love programming.\n')
    # многострочная запись:
    file_object.write('I love creating new games.\n')

# Файлы можно открывать в режиме чтения ('r'), записи ('w'), присоединения ('a') или в режиме,
# допускающем как чтение, так и запись в файл ('r+')

print('\nПрисоединение данных к файлу:\n')

filename = 'programming.txt'
# аргумент 'a' используется для открытия файла в режиме присоединения
# (вместо перезаписи существующего файла):
with open (filename, 'a') as file_object:
# далее записываются две новые строки, которые добавляются к содержимому programming.txt:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')
