# работая с несколькими файлами, проще всего определить функции,
# которые будут отвечать за чтение разных файлов в одной программе

def count_words(filename):
    """Подсчет приблизительного количества строк в файле"""
    try:
	    with open(filename, encoding='utf-8') as file_object:
		    contents = file_object.read()
    except FileNotFoundError:
	    msg = "Sorry, the file " + filename + " is not found"
	    print(msg)
    else:
	    words = contents.split()
	    num_words = len(words)
	    print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'the_whale.txt', 'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

print('\nОшибки без уведомления пользователя\n')

# Иногда при возникновении исключения программа должна просто проигнорировать сбой и продолжать работу,
# Для этого блок try пишется так же, как обычно, но в блоке except вы приказываете Python,
# не предпринимать никаких особых действий в случае ошибки, путем использования команды pass:

def count_words(filename):
    """Подсчет приблизительного количества строк в файле"""
    try:
	    with open(filename, encoding='utf-8') as file_object:
		    contents = file_object.read()
    except FileNotFoundError:
	    pass
    else:
	    words = contents.split()
	    num_words = len(words)
	    print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'the_whale.txt', 'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# в данном случае, программа не выдает данные об отсутствии файла

