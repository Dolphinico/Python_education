print('Набор классов для представления электромобилей\n')
from car import Car

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