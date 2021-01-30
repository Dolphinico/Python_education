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
