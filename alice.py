filename = 'alice.txt'

# with open (filename) as file_object:
#     contents = file_object.read()

# В данном примере функция open() порождает ошибку,
# и, чтобы обработать ее, блок try начинается перед строкой с вызовом open():

try:
    with open (filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + " does not exist."
    print(msg)

# В этом примере код блока try выдает исключение FileNotFoundError,
# поэтому Python ищет блок except для этой ошибки.
# Затем выполняется код этого блока, в результате чего вместо трассировки выдается доступное сообщение об ошибке.

print('\nАнализ текста\n')

# для примера будет взят текст книги Alice in Wonderland
# при помощи метода split(), который разделяет строку на части по всем позициям,
# в которых обнаружит пробел, и сохраняет все части строки в элементах списка,
# попробуем подсчитать количество слов в тексте:

try:
    with open (filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + " does not exist."
    print(msg)
else:
# подсчет приблизительного количества строк в файле:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")