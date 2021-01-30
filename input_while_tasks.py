print('\nУпражнение 7-1')

#cars = '\nWelcome to our car sharing service!'
#cars += '\nWhich car you wanna rent? '
#share = input(cars)
#print('Let me see if I can find you a ' + share)

print('\nУпражнение 7-2')

#greeting = input('Welcome to our restourant, whats your name? ')
#print('\nNice to meet you ' + greeting)
#rent = input('\nHow many seats you wanna rent? ')
#rent = int(rent)
#if rent > 8:
    #print('\nSorry, but u need to wait a little bit for it')
#else:
    #print('\nYour table is ready, have a sit and rest!')


print('\nУпражнение 7-3')

#numbers = input('\nEnter a number, i will tell you, odd it or even: ')
#numbers = int(numbers)
#if numbers % 10 == 0:
    #print('\nThe number ' + str(numbers) + ' is even.')
#else:
    #print('\nThe number ' + str(numbers) + ' is odd.')

print('\nУпражнение 7-4')

#pizza_toppings = "\nHello, which topping you wanna add in pizza?"
#pizza_toppings += "\n(Please, enter 'quit' if you are finished your order.) "

#while True:
    #toppings = input(pizza_toppings)
    #if toppings == 'quit':
        #break
    #else:
        #print('\n' + toppings.title() + ' will be added in your pizza!')

print('\nУпражнение 7-5') 

#message = "\nPlese enter your 'age' here: "

#while True:
    #inputStr = input(message)
    #if inputStr == 'quit':
        #print('\nbb, loser xd')
        #break
    #age = int(inputStr)
    #if age <= 3:
        #print('\nTicket will be free for you, have a nice day!')
    #elif age >= 3 and age <= 12:
        #print('\nTicket will cost 10$ for you, have a nice day!')
    #else:
        #print('\nTicket will cost 15$ for you, have a nice day!')

print('\nУпражнение 7-6') 

print('\nЗавершение цикла по проверке условия в команде while\n') 

#toppings = "\nВведите топинг который вы хотите добавить."
#toppings += "\n(Если закончили введите 'quit') "
#message = ''

#while message != 'quit':
    #message = input(toppings)
    #if message != 'quit':
        #print(message)

print('\nУправление продолжительностью выполнения цикла в зависимости от переменной active\n') 

#toppings = "\nВведите топинг который вы хотите добавить."
#toppings += "\n(Если закончили введите 'quit) "

#active = True

#while active:
    #message = input(toppings)
    #if message == 'quit':
        #active = False
    #else:
        #print(message)

#print('\nВыход из цикла по команде break, если пользователь вводит значение ‘quit’\n') 
#pizza_toppings = "\nHello, which topping you wanna add in pizza?"
#pizza_toppings += "\n(Please, enter 'quit' if you are finished your order.) "

#while True:
    #toppings = input(pizza_toppings)
    #if toppings == 'quit':
        #break
    #else:
        #print('\n' + toppings.title() + ' will be added in your pizza!')

print('\nУпражнение 7-8')

#sandwich_orders = ['бокадильо', 'арепа', 'крок-мадам', 'бан Ми', 'донер-кебаб', 'вада пав']
#finished_sandwhiches = []

#while sandwich_orders:
    #finished_sandwhich = sandwich_orders.pop()
    #print('Список сэндвичей которые можно сделать: ' + finished_sandwhich.title() + '\n')
    #finished_sandwhiches.append(finished_sandwhich)

#for sandwich in finished_sandwhiches:
    #print('Я сделал для тебя ' + sandwich.title() + '!')


print('\nУпражнение 7-9')

#sandwich_orders = ['бокадильо', 'пастрами', 'крок-мадам', 'пастрами', 'донер-кебаб', 'пастрами']
#finished_sandwhiches = []
#print('\nСэмичи пастрами закончились sadKEK.\n')
#while 'пастрами' in sandwich_orders:
    #sandwich_orders.remove('пастрами')

#while sandwich_orders:
    #finished_sandwhich = sandwich_orders.pop()
    #print('Список сэндвичей которые можно сделать: ' + finished_sandwhich.title() + '\n')
    #finished_sandwhiches.append(finished_sandwhich)

#for sandwich in finished_sandwhiches:
    #print('Я сделал для тебя ' + sandwich.title() + '!')

print('\nУпражнение 7-10')

responses = {}
poll_active = True
while poll_active:
    name = input('\nКак звать солдат? ')
    place = input('\nГде хотел бы отдохнуть? ')

    responses[name] = place

    repeat = input('Пустить следующего отвечать? (да / нет) ')
    if repeat == 'нет':
        poll_active = False

print('\n--- Результаты опроса ---')
for name, place in responses.items():
    print(name + ' хотел бы почилить ' + place + '.')


