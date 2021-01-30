alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#отслеживание передвижения объекта

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#alien_0['speed'] = 'fast'
print('Original x-position: ' + str(alien_0['x_position']))
#В данном примере пришелец перемещяется вправо
#теперь определим величину смещения на основании текущей скорости
if alien_0['speed'] == 'slow': #цепочка if-elif-else определяет, на какое расстояние пришелец должен, переместиться вправо; полученное значение сохраняется в переменной x_increment
    x_incresment = 1
elif alien_0['speed'] == 'medium':
    x_incresment = 2
else:
    x_incresment = 3 #пришелец двигается быстро
#новая позиция пришельца равна сумме старой позиции и наращивания:
alien_0['x_position'] = alien_0['x_position'] + x_incresment

print('New position: ' + str(alien_0['x_position']))
print(alien_0)

print('Вложение Aliens\n')

alien_0 = {'color': 'green', 'points': '5' }
alien_1 = {'color': 'yellow','points': '10' }
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#создание "флота" при помощи метода range()
print('\nсоздание "флота" при помощи метода range()\n')
#сначала создается пустой список:
aliens = []
#создание флота из 30 пришельцев:
for alien_number in range(30): #<- функция range() указывает python сколько раз цикл должен повториться,
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #при каждом повторе создается именно этот пришеле(либо другой указанный)
    aliens.append(new_alien)
#Например, чтобы превратить первых трех пришельцев в желтых,
#двигающихся со средней скоростью и приносящих игроку по 10 очков, либо в быстрых по 15 очков можно
#действовать так:
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

#вывод первых 5 пришельцев при помощи среза (slice):
for alien in aliens[:5]:
    print(alien)
print('...')
#вывод точного количества созданных пришельцев:
print('Total number of aliens: ' + str(len(aliens)))

#Все пришельцы обладают одинаковыми характеристиками, но Python рассматри-
#вает каждого пришельца как отдельный объект, что позволяет изменять атрибуты
#каждого владельца по отдельности.