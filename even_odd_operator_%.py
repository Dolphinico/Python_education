print('\nОператор вычисления остатка\n')
#Оператор вычисления остатка

#оператор вычисления остатка (%), ообщает частное от целочисленного деления; он возвращает только
#остаток.
#пример где это может пригодится:

number = input('Enter a number, and I will tell you is it even of odd: ')
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')
    
#если остаток от деления на 2 равен 0 (number % 2 == 0), число четное, а если нет — нечетное    