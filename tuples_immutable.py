#Кортеж - tuple, неизменяемый (immutable) список объектов
#пример обьеденения кортежей для условного прямоугольника
dimensions = (200,50)
#dimensions[0] = 250 в данном случает питон выдает ошибку чтения программы, так как кортеж - не может быть изменен
print(dimensions [0])
print(dimensions [1])
#перебор значений в кортеже осуществляется по такому же принципу как и в обычном списке, через функцию for например

dimensions = (200,50)
print("Original dimensions")
for dimension in dimensions:
	print(dimension)
#пример правильной замены кортежей
dimensions = (400,150)
print("\nModified dimensions")
for dimension in dimensions:
	print(dimension)
