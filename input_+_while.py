#Ввод данных и циклы while
print('\nВвод данных input() и циклы while')

#message = input('Tell me something i will repeat it back to you: ') #Функция input() получает один аргумент: текст подсказки (или инструкции),
#который выводится на экран, чтобы пользователь понимал, что от него требуется.
#как работает код см. repeater.py

#Содержательные подсказки

#name = input('Please print your name: ')
#print('Hello ' + name +'!') как работает код см. в greater.py

#для отображения подсказки более чем в одну строку можно сохранить ее в переменной и передать переменную в input()

#prompt = 'If you tell us who you are, we can personalize the messages you see.'
#prompt += '\nWhat is your first name? '

#name = input(prompt)
#print('Hello ' + name + '!')
#как работает код см. в greater.py

#Допустим, программа проверяет рост пользователя и определяет, достаточен ли он для катания на аттракционе:
#height = input('How tall are you? In inches ')
#height = int(height)

#if height >= 36:
    #print('\nYou are tall enough to ride on rollercoasters!')
#else:
    #print("\nYou'll be able to ride when you're a little older.")

#см. работу кода usint_int_with_input.py

print('\nОператор вычисления остатка\n')
#Оператор вычисления остатка

#оператор вычисления остатка (%), ообщает частное от целочисленного деления; он возвращает только
#остаток.
#пример где это может пригодится:

#number = input('Enter a number, and I will tell you is it even of odd: ')
#number = int(number)

#if number % 2 == 0:
#    print('\nThe number ' + str(number) + ' is even.')
#else:
#    print('\nThe number ' + str(number) + ' is odd.')
# работы программы см. even_odd_operator_%.py

print('\nЦиклы while\n')

#В отличие от цикла for  который выполняет блок кода один раз , цикл while продолжает вы-
#полняться, пока остается истинным некоторое условие.

print('\nCounting пример\n')

#Цикл while может использоваться для перебора числовой последовательности.
#Например, следующий цикл считает от 1 до 5:
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 #Оператор += является сокращенной формой записи для current_number = current_number + 1.)

print('\nПример завершения работы пользователем\n')

quick = "\nTell me something, and i'll repeat it back to you:"
quick += "\nEnter 'quit' to end the programm. "
message = ""
while message != 'quit':
    message = input(quick)
    if message != 'quit':
        print(message)

#что бы при в вводе quit сообщение не дублировалось, а выполнялась команда, можно добавить простую проверку if

print('\nФлаги, для сложных программ с несколькими условиями\n')

#Если программа должна выполняться только при истинности нескольких условий,
#определите одну переменную - флаг, см flags.py

print('\nКоманда break и выход из цикла\n')

#Команда break и выход из цикла, позволяет управлять, тем, какая часть кода выполняется, какая нет.
#break_exaample.py

print('\nКоманда continue и продолжение цикла\n')
#continue_example.py

print('\nИспользование цикла while со списками и словарями\n')
#while_+_dictionarys.py - примеры кода

print('\nУдаление всех вхождений конкретного значения из списка\n')
#пример работы программы, на удалении конкретного занчения, которое повторяется много раз в списке remove_while.py

print('\nЗаполнение словаря данными, введенными пользователем\n')
#пример работы программы filling_by_user.py