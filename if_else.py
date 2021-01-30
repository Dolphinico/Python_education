#Команды if \ else 
print('\nКоманды if / else')

cars = ['subaru','toyota','bmw','audi']
for car in cars:
	if car == 'bmw':
		print(car.upper()) #в данном случае указано условие, что если при выполнении цикла for будет объект bmw то он будет написан в верхнем регистре, если нет, то объект будет записан с заглавной буквы
	else:
		print(car.title()

#проверка неравенства при помощи комбинации (!=), пример приведен в виде заказа пицы, заказ был сделан только с 'mushrooms' и если появляется 'anchovies' то программа выдает сообщение 'hold the anchovies' тк они не были в заказе

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
	print('hold the anchovies')

#сравнение чисел, в примере указана ситуация где указано неверное число и программа останавливается с выводом сообщения
print('\nСравнение чисел')

answer = '7'
if answer != '47':
	print('Thats the wrong number, try again!')

#проверка несколькких условий через and \ or

#проверка через and
print('\nПроверка через and')

a = age_0 = 22
b = age_1 = 18
c = (age_0 >= 21) and (age_1 >= 21) #в данном случае выражение будет False, так как одна из переменных является не верной
print(c)
s = age_1 = 22
x = (age_0 >= 21) and (age_1 >= 21)
print(x)

#проверка через or
print('\nПроверка через or')

a = age_0 = 22
b = age_1 = 18
c = (age_0 >= 21) or (age_1 >= 21) #в данном случае выражение будет True, так как одна из переменных является верной
print(c)
s = age_0 = 18
x = (age_0 >= 21) or (age_1 >= 21) #в данном случае выражение будет False, так как обе переменных меньше 21
print(x)

#проверка вхождения значений в список при помощи ключевого слова in

print('\nПроверка вхождения значений в список при помощи ключевого слова in')

a = requested_toppings = ['mushrooms','onions','pineapple','apple']
b = 'mushrooms' in requested_toppings #выдает значение True, тк грибы есть в изначальном списке
x = 'pepperoni' in requested_toppings #выдает значение False, тк пеперони нет в списке
print(x,b)

#проверка отсутствия значения в списке иcпользуя ключевое слово not
print('\nПроверка отсутствия значения в списке иcпользуя ключевое слово not')

banned_users = ['slo','joe','poe','moe']
user = 'marie'
if user not in banned_users: #в данном примере если пользователь не в списке забаненных, то он увидит сообщение ниже
	print(user.title() + ', you can respond if you wish.')

#Логическое выражение всегда равен True или False
