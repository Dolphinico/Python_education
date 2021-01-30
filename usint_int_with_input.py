#Допустим, программа проверяет рост пользователя и определяет, достаточен ли он для катания на аттракционе:

height = input('How tall are you? In inches ')
height = int(height)

if height >= 36:
    print('\nYou are tall enough to ride on rollercoasters!')
else:
    print("\nYou'll be able to ride when you're a little older.")