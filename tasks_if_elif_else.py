# Задания по блоку if-elif-else
print('Задания по блоку if-elif-else\n')
#версия с выводом сообщения и 'True'

alien_color = 'green'

if 'green' in alien_color:
    print('Congratulation u won 5 points!') 

#версия без вывода сообщения и 'False'

alien_color = 'green'

if 'green' in alien_color:
    print('Congratulation u won 5 points!') 
if 'yellow' in alien_color:
    print()

#цепочка if-else
print('\nЦепочка if-else\n')

#простой вариант  в двух программах
alien_color = 'green'

if 'green' in alien_color:
    print('Congrats u won 5 poitns!')

alien_color = 'red'

if 'green' in alien_color:
    print('Congrats u won 5 poitns!')
else:
    print('Congrats u won 10 poitns!')

#вариант где выводится сообщение о тру цвете - вывод 5 очков, если любой другой - 10 очков (сложный)

alien_color = ['green','yellow','red']

for color in alien_color:
    if color == 'green':
        print('Congrats u won 5 points!')
else:
    print('Congrats u won 10 points!\n')

#вариант в котором выполняется только цепочка else и выводом сообщения на 10 очков

alien_color = ['yellow','red']

if 'green' in alien_color:
    print('Congratulation u won 5 points!\n')
else:
    print('Congratulation u won 10 points!\n')

alien_color = ['green','yellow','red']

if 'green' in alien_color:
    print('Congratulation u won 5 points!\n')
else:
    print('Congratulation u won 10 points!\n')

#преобразование цепочки if-else в цепочку if-elif-else 5-5
print('\nпреобразование цепочки if-else в цепочку if-elif-else\n')

alien_color = ['green','yellow','red']

for color in alien_color:
    if color == 'green':
        print('Congratulation u won 5 points!\n')
    elif color == 'yellow':
        print('Congratulation u won 10 points!\n')
    elif color == 'red':
        print('Congratulation u won 15 points!\n')

#Цикл жизни человека 5-6
print('\nЦикл жизни человека\n')

age = 14 #указывая число от 1 до 66 и больше будет изменяться результат

if age < 2:
    print('Младенец')
elif age >= 2 and age < 4:
    print('Малыш')
elif age >= 4 and age < 13:
    print('Ребенок')
elif age >= 13 and  age < 20:
    print('Подросток')
elif age >= 20 and age < 65:
    print('Взрослый')
else:
    print('Пожилой')

#5-7

favorite_fruits = ['banana','apple','orange','kivi','peach']

print('\nMy favorite fruits is: \n')
for fruit in favorite_fruits:
    print(fruit.title() + '!')

if 'banana' in favorite_fruits:
    print('You really like Banana!')
if 'apple' in favorite_fruits:
    print('You really like Apples!')
if 'pineapple' in favorite_fruits:
    print('Nah i dont like it')
if 'orange' in favorite_fruits:
    print('You really like Oranges!')
if 'peach' in favorite_fruits:
    print('You really like Peach!')
if 'waterlemon' in favorite_fruits:
    print('BUEH')
else:
    print('\nI love all the fruits beacuse its healthy')

#5-8 упражнение

print('\n5-8 упражнение\n')

hello_admin = ['admin','sanya','romanich','tema','daniil','vasya']

for hello_admin in hello_admin:
    if hello_admin == 'admin':
        print('Hello ' + hello_admin.title() + ', would you like to see a status report?')
    else:
        print('Hello ' + hello_admin.title() + ' thank you for logging in again.')

print('\n5-9 упражнение\n')

hello_admin = [] #если внести хотя бы один объект в список, будет выполнятся цикл for, тк if будет true

if hello_admin:
    for hello_admin in hello_admin:
        print('The list is not empty!')
else:
    print('We need to find some users!')

print('\n5-10 упражнение\n')
#
current_users = ['Sanya','Roman','Tema','Daniil','Vasya']
new_users = ['Oleg','Sanya','Valera','Daniil','Maksim'] #если вводить имя с маленькой буквы либо всеми заглавными, 
#и оно есть в списке, будет выведено сообщение о том что такой ник занят.

for new_users in new_users:
    if new_users in current_users:
        print(new_users + ' you should change the name.')
    elif new_users == new_users.lower():
        print('You cant use this name, its already used.')
    elif new_users == new_users.upper():
        print('You cant use this name, its already used.')
    else:
        print('This name are available: ' + new_users)

print('\n5-11 упражнение\n')

digits = [1,2,3,4,5,6,7,8,9]
for digit in digits:
    if digit == 1:
        print(str(digit) + 'st')
    elif digit == 2:
        print(str(digit) + 'nd')
    elif digit == 3:
        print(str(digit) + 'rd')
    else:
        print(str(digit) + 'th')
    
    
