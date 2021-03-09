print("Give me two numbers, and I'll summ them.")
print("Enter 'q' to quit")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('Please, type a digit with numbers')
    else:    
        print(answer)