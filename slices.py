#работа со срезами списков (slices)
#создание среза
players = ['jojo','lulu','lala','dodo','dudu','gaga','hehe',]
print(players[0:3])

#что бы ограничить список например только 2 обьъектами, указывается ID объектов в необходимом интервале ex. [2:4]
players = ['jojo','lulu','lala','dodo','dudu','gaga','hehe',]
print(players[1:4])

#перебор содержимого среза списка
players = ['jojo','lulu','lala','dodo','dudu','gaga','hehe',]
print("Here are the first three players of my list: ")
for player in players[:3]:
	print(player.title())
	
#копирование списков
my_foods = ['pizza','burger','salami','snack','kebab']
friends_foods = my_foods[:]
my_foods.append ("milk") #пример того что копируется изначальный список, а затем его можно видоизменять под свои нужды
friends_foods.append ("tea")
print("My favorite foods are :")
print(my_foods)
print("\nMy friend's favorite foods are :")
print(friends_foods)

