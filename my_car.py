from car import Car

# import приказывает Python открыть модуль car и импортировать класс Car.
# Теперь мы можем использовать класс Car так, как если бы он был определен в этом файле.

my_new_car = Car('audi', 'a3','2020')
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 23
my_new_car.read_odometer()

