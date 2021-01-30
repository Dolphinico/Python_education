import sys
import random
from msvcrt import getch
 
number = random.randint(1, 100)
 
while True:
    guess = int(input('Введите целое число : '))
 
    if guess < number:
        print('Нет, загаданное число немного больше этого.')
 
    elif number == guess:
        print('Поздравляю, вы угадали,')
        print('(хотя и не выиграли никакого приза!)')
 
    else:
        print('Нет, загаданное число немного меньше этого.')
 
    print('Завершено')
    print('Для выхода нажмите Enter')
    exit = ord(getch())
    if exit == 13:
        break
