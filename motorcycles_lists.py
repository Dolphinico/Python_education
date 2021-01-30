motorcycles = ['honda','suzuki','yamaha']
motorcycles[0]= 'ducati' #в таком случае объект honda[0], заменяется на обьект ducati[0]
print(motorcycles)

motorcycles = ['honda','suzuki','yamaha',]
print(motorcycles)
motorcycles.append('ducati') #метод append - добавляет новый пунк в списке, которго не было изначально.
print(motorcycles)

motorcycles = []
motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles = ['honda','suzuki','yamaha']
motorcycles.insert(0, 'dukati') #метод .insert - добавляет в уже существующий список новый обьект, остальные при этом смещаются вправо на одну позицию
print(motorcycles)

motorcycles = ['honda','suzuki','yamaha']
print(motorcycles)
motorcycles = ['honda','suzuki','yamaha']
del motorcycles[0] #метод del - может удалять объект, если известен его индекс/id
print(motorcycles)


motorcycles = ['honda','suzuki','yamaha']
print(motorcycles) 

popped_motorcycle = motorcycles.pop() #метот pop() позволяет извлечь объект из списка, а затем снова использовать его, если он был добавлен в новую переменную
print(motorcycles) 
print(popped_motorcycle)


motorcycles = ['honda','suzuki','yamaha']
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.') #в данном случае в переменной last_owned хранится последний объект из списка (yamaha)

first_owned = motorcycles.pop(0) #в этом случае в переменной привязан конкретный объект по его индексу
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


motorcycles = ['honda','suzuki','yamaha','ducati']
print(motorcycles) 
motorcycles.remove('ducati') #.remove - удаляет указанный обьект из списка
print(motorcycles)

motorcycles = ['honda','suzuki','yamaha','ducati']
print(motorcycles) 
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print('motorcycles')
print("\nA " + too_expensive.title() + " is too expensive for me.")








