print('Вывод всего текста:\n')

filename = ('text_files/hokku.txt')
with open (filename) as file_object:
    contents = file_object.read()
    print(contents)

print('\nВывод всего текста с перебором строк объекта файла и с сохранением строк в списке:\n')

filename = ('text_files/hokku.txt')
with open (filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\nВывод всего текста с последующим выводом списка вне блока with:\n')

filename = ('text_files/hokku.txt')
with open (filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

