print("Give me two numbers, and I'll summ them.")

x = input('\nFirst number: ')
y = input('\nSecond number: ')

try:
    summ = int(x) + int(y)
except ValueError:
    print('Please, type a digit with numbers')
else:
    print(summ)
