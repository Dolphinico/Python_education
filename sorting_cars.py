#метод для сортировки списка в алфавитном порядке
cars = ["бмв", "субару", "тойота", "ауди"]
cars.sort() 
print(cars)

#обратный порядок сортировки
cars.sort(reverse=True)
print(cars)
#временная сортировка списка
cars = ["бмв", "субару", "тойота", "ауди"]
print("\nHere is original cars list:")
print(cars)
print("\nHere is the sorted cars list:")
print(sorted(cars))
print("\nHere is original cars list again:")
print(cars)
#обратный порядок сортировки методом .reverse()
cars = ["бмв", "субару", "тойота", "ауди"]
print(cars)
cars.reverse()#реверсить можно в обе стороны, применяя метод .reverse() к тому же списку
print(cars)

#определение длинны списка методом len()
cars = ["бмв", "субару", "тойота", "ауди"]
len(cars) #команда срабатывает напрямую в IDLE

