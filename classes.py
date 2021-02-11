print('Создание и использование класса:\n')

class Dog(): 
# определяем класс - Dog, общепринято называть класс с верхнего регистра
# скобки пусты, тк класс создается с нуля
    """Простая модель собаки."""
    def __init__(self, name, age):
# метод __init__ - специальный метод автоматически выполняется при создании каждого нового экземпляра
# на базе класса Dog.
# параметр (self) обязателен
        """Инициализирует атрибуты name и age."""
        self.name = name 
        self.age = age
# Конструкция self.name = name берет значение, хранящееся в параметре name, 
# и сохраняет его в переменной name, которая затем связывается с создаваемым экземпляром, тоже самое с self.age
    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака делает перекат по команде."""
        print(self.name.title() + ' rolled over!')
#  В классе Dog также определяются два метода: sit() и roll_over()
#  Так как этим методам не нужна дополнительная информация (кличка или возраст),
#  они определяются с единственным параметром self.

# cоздадим экземпляр, представляющий конкретную собаку:

my_dog = Dog('maki', 4) 
# тут мы приказываем Python создать экземпляр собаки с кличкой 'willie' и возрастом 6.
print("My dog's name is " + my_dog.name.title() + ".") 
# мы обращаемся к значению атрибута name экземпляра my_dog.
print("My dog is " + str(my_dog.age) + " years old.") 
# мы обращаемся к значению атрибута age экземпляра my_dog + преобразуем 6(age) в строку (str)

# теперь вызываем методы, описанные в функциях sit и roll_over:

my_dog.sit()
my_dog.roll_over()

# создадим новый экземпляр:

your_dog = Dog('sandy', 6)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()

print('\nРабота с классами и экземплярами, \nназначение атрибуту значения по умолчанию,\nизменение значений атрибутов\n')

# пример такой работы с новым классом:

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания авто"""
        self.make = make
        self.model = model
        self.year = year
# на основе этого же примера мы назначяем атрибуту значения по умолчанию
# добавим новый атрибут с исходным значением всегда равному 0:
        self.odometer_reading = 0
    def get_descriptive_name(self): 
# здесь мы определяем метод get_descriptive_name(), который объединяет год выпуска,
# фирму-производителя и модель в одну строку с описанием. 
# Это избавит нас от необходимости выводить значение каждого атрибута по отдельности
        """Возвращает аккуратно отформатированное описание"""
        long_time = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time.title()
    def read_odometer(self):
        """Выводит пробег машины в км"""
        print("This car has " + str(self.odometer_reading) + " kilometers on it")

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# изменять атрибуты можно тремя способами:
#  1. изменить его прямо в экземпляре
#  2. задать значение при помощи метода 
#  3. изменить его с приращением (то есть прибавлением определенной величины) при помощи метода

print('\nпример изменения значения атрибута прямо в экземпляре:\n')

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания авто"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self): 
        """Возвращает аккуратно отформатированное описание"""
        long_time =str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time.title()
    def read_odometer(self):
        """Выводит пробег машины в км"""
        print("This car has " + str(self.odometer_reading) + " kilometers on it")

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 200
my_new_car.read_odometer()

print('\nпример изменения значения атрибута с использованием метода:\n')

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания авто"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self): 
        """Возвращает аккуратно отформатированное описание"""
        long_time =str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time.title()
    def read_odometer(self):
        """Выводит пробег машины в км"""
        print("This car has " + str(self.odometer_reading) + " kilometers on it")
    # вместо изменения атрибута напрямую, мы передаем новое значение методу,
    #  который берет обновление атрибута на себя
    def update_odometer(self, mileage):
        """Устанавливаем заданное значение на одометре"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(250)
my_new_car.read_odometer()

print('\nпример более сложного класса, с условием:\n')

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания авто"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1000
    def get_descriptive_name(self): 
        """Возвращает аккуратно отформатированное описание"""
        long_time =str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time.title()
    def read_odometer(self):
        """Выводит пробег машины в км"""
        print("This car has " + str(self.odometer_reading) + " kilometers on it")
    def update_odometer(self, mileage):
        """
        Устанавливаем заданное значение на одометре.
        При попытке скрутки одометра, изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer!')

# теперь update_odometer() проверяет новое значение перед изменением атрибута.
# если новое значение mileage больше или равно текущего, self.odometer_reading,
# показания одометра можно обновить новым значением. 
# если новое значение меньше текущего, вы получите предупреждение о недопустимости скрутки

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(999)
my_new_car.read_odometer()

print('\nпример изменения значения атрибута с приращиванием, при помощи метода:\n')

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания авто"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self): 
        """Возвращает аккуратно отформатированное описание"""
        long_time =str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time.title()
    def read_odometer(self):
        """Выводит пробег машины в км"""
        print("This car has " + str(self.odometer_reading) + " kilometers on it")
    def update_odometer(self, mileage):
        """Устанавливаем заданное значение на одометре"""
        self.odometer_reading = mileage
# новый метод increment_odometer() теперь получает расстояние в километрах
# и прибавляет его к self.odometer_reading:
    def incresment_odometer(self, kilometers):
        """Увеличивает покозания одометра с приращиванием"""
        self.odometer_reading += kilometers

my_used_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())

my_used_car.update_odometer(100000)
my_used_car.read_odometer()

my_used_car.incresment_odometer(50000)
my_used_car.read_odometer()