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