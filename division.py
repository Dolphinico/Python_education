# Если вы предполагаете, что в программе может произойти ошибка, напишите блок
# try-except для обработки возникающего исключения

# пример кода с блоком try-except:

try:
    print(5/0)
except ZeroDivisionError:
    print('You cant devide by zero!')

print('\nИспользование исключений для предотвращения аварийного завершения программы\n')

# Создадим простой калькулятор, который выполняет только операцию деления:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break
#     second_number = input('\nSecond number: ')
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

# Для повышения устойчивости программы к ошибкам можно заключить строку,
# выдающую ошибки, в блок try-except. Ошибка происходит в строке, выполняющей
# деление; следовательно, именно эту строку следует заключить в блок try-except.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant devide by zero!')
    else:    
        print(answer)



