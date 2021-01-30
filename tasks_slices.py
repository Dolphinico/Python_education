#упражнения по главе slices
my_foods = ['pizza','burger','salami','snack','kebab']
print("The first three items in list are: ")
for food in my_foods[:3]:
	print(food.title())

my_foods = ['pizza','burger','salami','snack','kebab']
print("The three items in the middle of the list are: ")
for food in my_foods[1:4]:
	print(food.title())

my_foods = ['pizza','burger','salami','snack','kebab']
print("The last three items in list are: ")
for food in my_foods[2:]:
	print(food.title())

friend_pizzas = ["Пепперони","Четыре сыра","Чикен ранч"]
my_pizzas = friend_pizzas[:]
friend_pizzas.append("чеддер")
my_pizzas.append("маргарита")
print("My favorite pizzas is: ")
for pizza in my_pizzas:
	print(pizza.title())
print("\nMy friends favorite pizzas is: ")
for pizza in friend_pizzas:
	print(pizza.title())
