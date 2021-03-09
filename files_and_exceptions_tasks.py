print('Упражнение 10-1\n')

# Откройте пустой файл в текстовом редакторе и напишите несколько строк текста о возможностях Python.
# Каждая строка должна начинаться с фразы: «In Python you can…».
# Сохраните файл под именем learning_python txt в каталоге, использованном для примеров этой главы.
# Напишите программу, которая читает файл и выводит текст три раза:
# с чтением всего файла, с перебором строк объекта файла и с сохранением строк в списке
# с последующим выводом списка вне блока with
# задача выполнена в hokku_reader.py

print('Упражнение 10-2\n')

# Изучение C: метод replace() может использоваться для замены любого слова в строке
# другим словом В следующем примере слово ‘dog’ заменяется словом ‘cat’:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Прочитайте каждую строку из только что созданного файла learning_python txt и замените
# слово Python названием другого языка, например C Выведите каждую измененную строку на экран
# задача выполнена в replace_words.py

print('Упражнение 10-3\n')

# Гость: напишите программу, которая запрашивает у пользователя его имя
# Введенный ответ сохраняется в файле с именем guest.txt
# задача выполнена в файле guest.py

print('Упражнение 10-4\n')

# Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей имена
# При вводе каждого имени выведите на экран приветствие и добавьте строку с сообщением в файл с именем guest_book.txt
# Проследите за тем, чтобы каждое сообщение размещалось в отдельной строке файла
# задача выполнена в файле guests_book.py

print('Упражнение 10-5\n')

# Опрос: напишите цикл while, в котором программа спрашивает у пользователя, почему ему нравится программировать
# Каждый раз, когда пользователь вводит очередную причину, сохраните текст его ответа в файле.
# задача выполнена в файле love_to_programming.py

print('Упражнение 10-6\n')

# Сложение: при вводе числовых данных часто встречается типичная проблема: пользователь вводит текст вместо чисел.
# При попытке преобразовать данные в int происходит исключение TypeError.
# Напишите программу, которая запрашивает два числа, складывает их и выводит результат.
# Перехватите исключение TypeError, если какое-либо из входных
# значений не является числом, и выведите удобное сообщение об ошибке.
# Протестируйте свою программу: сначала введите два числа, а потом введите текст вместо одного из чисел.
# задача выполнена в файле summ_calc.py

print('Упражнение 10-7\n')

# Калькулятор: заключите код из упражнения 10-6 в цикл while, чтобы пользователь
# мог продолжать вводить числа, даже если он допустил ошибку и ввел текст вместо числа
# задача выполнена в файле calculator_with_error.py

print('Упражнение 10-8/9\n')

# Кошки и собаки: создайте два файла с именами cats txt и dogs txt.
# Сохраните минимум три клички кошек в первом файле и три клички собак во втором.
# Напишите программу, которая пытается прочитать эти файлы и выводит их содержимое на экран.
# Заключите свой код в блок try-except для перехвата исключения FileNotFoundError и вывода понятного
# сообщения об отсутствии файла
# Переместите один из файлов в другое место файловой системы;
# убедитесь в том, что код блока except выполняется, как и положено.
# задача выполнена в файле cats_and_dogs.py

print('Упражниение 10-10\n')

# Частые слова: зайдите на сайт проекта «Гутенберг» (http://gutenberg org/) и найдите
# несколько книг для анализа.
# Загрузите текстовые файлы этих произведений или скопируйте текст из браузера в текстовый файл на вашем компьютере.
# Для подсчета количества вхождений слова или выражения в строку можно воспользоваться методом count().
# Например, следующий код подсчитывает количество вхождений ‘row’в строке:

# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Обратите внимание: преобразование строки к нижнему регистру функцией lower()
# позволяет найти все вхождения искомого слова независимо от регистра
# Напишите программу, которая читает файлы из проекта «Гутенберг»
# и определяет количество вхождений слова ‘the’ в каждом тексте.
# задава выполнена в frequent_words.py