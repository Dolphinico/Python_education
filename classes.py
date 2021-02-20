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

print('\nНаследование\n')

# Один класс, наследующий от другого, автоматически получает все атрибуты и методы первого класса
# пример на уже существующем классе Car.py

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

class ElectricCar(Car):
    """Представляет аспекты специфичные для электромобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родтеля(Car)"""
        super().__init__(make, model, year)

# Функция super() — специальная функция, которая помогает Python
# связать потомка с родителем. Эта строка приказывает Python вызвать метод __init__() класса, 
# являющегося родителем ElectricCar, в результате чего экземпляр ElectricCar получает все атрибуты класса-родителя

my_tesla = ElectricCar('tesla','model - s', '2016')
print(my_tesla.get_descriptive_name())

# При создании класса-потомка класс-родитель (Car) должен быть частью текущего файла,
# а его определение должно предшествовать определению класса-потомка(ElectricCar) в файле.

print('\nОпределение атрибутов и методов класса-потомка\n')

# После создания класса-потомка, наследующего от класса-родителя, 
# можно переходить к добавлению новых атрибутов и методов,
# необходимых для того, чтобs потомок отличался от родителя. 
# Пример приведен ниже:

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

class ElectricCar(Car):
    """Представляет аспекты специфичные для электромобилей"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя(Car).
        Затем инициализирует атрибуты, специфические только для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery_size = 70 
# Этот атрибут будет присутствовать во всех экземплярах, 
# созданных на основе класса ElectricCar (но не во всяком экземпляре Car).

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla','model - s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print('\nЭкземпляры как атрибуты:\n')

# При моделировании явлений реального мира в программах,
# классы нередко дополняются все большим количеством подробностей.

# В такой ситуации часть одного класса нередко можно записать в виде отдельного
# класса. Большой код разбивается на меньшие классы, которые работают во взаимодействии друг с другом.

# Например, при дальнейшей доработке класса ElectricCar может оказаться, что
# в нем появилось слишком много атрибутов и методов, относящихся к аккумулятору.
# В таком случае можно остановиться и переместить все эти атрибуты и методы в отдельный класс с именем Battery.

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
#сначала определяем новый класс, который не наследует от других классов:
class Battery():
    """Простая модель аккумулятора электромобиля"""

    def __init__(self,battery_size = 70):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    # новый метод проводит простой анализ, если аккум = 70 то сообщение будет одно, если 85, то другое
    def get_range(self):
        """Выводит приблезительный запас аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " kilometers on a full charge."
        print(message)

class ElectricCar(Car):
    """Представляет аспекты специфичные для электромобилей"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя(Car).
        Затем инициализирует атрибуты, специфические только для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery() 
# добавляем атрибут self.battery, эта строка дает Python понять что нужно создать новый экземпляр Battery, 
# со значением battery_size = 70 заданным по умолчанию и сохранить его в атрибуте self.battery
# как итог, теперь каждый экзмепляр ElcetrcicCar будет автоматически создаваемый экземпляр Battery

my_tesla = ElectricCar('tesla','model - s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() # что бы вызвать этот метод, его нужно вызывать через .battery - так как он находится в нем

print("\nИмпортирование классов, хранение нескольких классов в модуле\n")

# Создаем модуль car.py, из него импортируем в my_car.py без лишнего кода
# Для хранения нескольих классов в модуле, все они должны быть как то связаны друг с другом.
# my_electric_car.py - тот же принцип что и с my_car.py