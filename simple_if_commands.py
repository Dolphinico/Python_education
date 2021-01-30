#Команды if,простые команды if
print('Команды if,простые команды if\n')

#age = int(input('Введите ваш возраст: ')) - моя версия, с участием юзера
age = 18
if age >= 18:
	print('Gratz u can vote now!')
	print('Have u registrated yet?')
		
#Команды if-else
print('\nКоманды if-else\n')

age = 17
if age >= 18:
	print('Gratz u can vote now!')
	print('Have u registrated yet?')
else:
	print('Sorry u, are too young for this!')
	print('Register to vote as u turn the 18!')
#Цепочки if-else-else

print('\nЦепочки if-else-else\n')
#age = int(input('Введите ваш возраст:'))
age = 12
if age <4:
	print('You may pass for free!') #пользователь увидит сообщение что он сможет войти бесплатно, если ему меньше 4 лет
elif age <18:
	print('You should pay 5$ to enter') #пользователь увидит сообщение что ему нужно заплатить 5$ за вход если ему меньше 18 лет
else:
	print('You should pay 10$ to enter')#все остальные возраста должны заплатить 10$ за вход
	
#компактный код, с теми же условиями
print('\nКомпактный код, с теми же условиями\n')

age = 12
if age <4:
	price = 0
elif age <18:
	price = 5
else:
	price = 10

print('Your admission cost is $' + str(price) + '.')

#Серии блоков elif
print('\nСерии блоков elif\n')

age = 70
if age <4:
	price = 0
elif age <18:
	price = 5
elif age <65:
	price = 5
else:
	price = 10

print('Your admission cost is $' + str(price) + '.')

#блок else не  всегда обязателен

age = 14
if age <4:
	price = 0
elif age <18:
	price = 5
elif age <65:
	price = 10
elif age >= 65:
	price = 5

print('Your admission cost is $' + str(price) + '.')

#Проверка нескольких условий if-elif-else

print('\nПроверка нескольких условий if-elif-else\n')

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')
if 'pepperoni' in requested_toppings: # пеперони не была добавлена в список, тк ее нет в изначальном списке 'requested_toppings', программа просто пропускает это условие и идет дальше.
	print('Adding pepperoni')

print('\nYour pizza is ready, have a nice meal!\n') #программа проверяет все условия, независимо 'True' они или 'False', она просто проводит сопоставление с изначальным списком.

#если добавить elif, то после первой проверки на 'True' / 'False' программа остановится и добавит только первый True

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings: 
	print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')

print('\nYour pizza is ready, have a nice meal!\n') #в цепочках if-elif-else после обнаружения первого истинного условия все остальные условия пропускаются.

#Использование команд if со списками и проверка специальных значений
print('\nИспользование команд if со списками + проверка специальных значений\n')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings: #цикл for перебирает список топингов в списке топингов и в итоге выводит все, что есть в списке ниже:
	print('Adding ' + requested_toppings + '.')
print("\nFinished making your pizza!\n")

#если в моделируемой ситуации отстутствует элемент из списка, команда if поможет правильно обработать ситуацию:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings:
	if requested_toppings == 'green peppers':
		print('Sorry we are out of green peppers right now.')
	else:
		print('Adding ' + requested_toppings + '.')
print("\nFinished making your pizza!")

#Проверка наличия элементов в списке:
print('\nПроверка наличия элементов в списке\n')
#в этом примере проверка начинается с пустого списка, программа начинает с if - но список пуст, 
# поэтому значение переходит к False и цикл for не запускается, так как программа пропускает его, 
# выявив False еще на первом шагу и выводит сообщение согласно if-else, но если добавить хотя бы один элемент в список,
#программа будет выполнятся полностью, так как одно из условий стало True

requested_toppings = []

if requested_toppings:
	for requested_toppings in requested_toppings:
		print('Adding ' + requested_toppings + '.')
		print("\nFinished making your pizza!")
else:
	print('Are you sure you want a plain pizza?')

#Множественные списки
print('\nМножественные списки\n')
#проверка нестандартных объектов на примере готовки пиццы:
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_toppings in requested_toppings:
	if requested_toppings in available_toppings:
		print('Adding ' + requested_toppings + '.')
	else:
		print('Sorry we dont have ' + requested_toppings + '.')
print('\nFinished making your pizza')

