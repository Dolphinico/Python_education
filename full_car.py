# строка документации уровня модуля с кратким описанием содержимого модуля:
"""Классы для представления автомобилей с бензиновым и электродвигателем""" 

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
    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

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
