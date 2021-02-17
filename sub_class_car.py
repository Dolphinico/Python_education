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
#  а его определение должно предшествовать определению класса-потомка(ElectricCar) в файле.

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