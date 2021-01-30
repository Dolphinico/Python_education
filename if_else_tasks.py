#упражнения по главе if\else 
print('\nПроверка равенства и неравенства строк')

game_1 = 'dota2'
game_2 = 'doka2'
print('\nIs game_1 == dota2? i predict "True"')
print(game_1 == 'dota2')
print('\nIs game_2 == Dota2? I predict "False"')
print(game_1 == 'doka2')
game_1 = 'foka2'
x = (game_1 == 'dota2') or (game_2 == 'doka2')
z = (game_1 == 'dota2') and (game_2 == 'doka2')

print('\nПроверки с ключевым словом and и or')
print(x)
print(z)

print('\nПроверка равества с .lower()')
a = game_1 = 'Dota2'
b = game_1.lower() == 'dota2'
c = game_1
print(c)

print('\nПроверка равенства и неравенства, условий больше, меньше, больше или равно,меньше или равно')
age_1 = 18
age_2 = 25
x = (age_1 >= 19) 
b = (age_1 >= 15)
n = (age_1 >= 19) or (age_2 <=24)
m = (age_1 == 18) and (age_2 == 25)
a = (age_1 <= 19)
s = (age_2 <= 23)
print(x)
print(b)
print(n)
print(m)
print(a)
print(s)

print('\nПроверка вхождения элемента в список')

a = game_list = ['dd','ss','aa','cc']
b = 'dd' in game_list
c = 'as' in game_list
print(b)
print(c)

print('\nПроверка отсутствия элемента в списке')

banned_games = ['aa','ss','dd','ff']
game = 'Dota2'
if game not in banned_games:
	print(game.title() + ' not in ban list, u allowed to play in this game!')

	




