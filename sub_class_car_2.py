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
            range = 300
        message = "This car can go approximately " + str(range)
        message += " kilometers on a full charge."
        print(message)

    def upgrade_battery(self):
        """Обновляет информацию о аккумуляторе"""
        if self.battery_size == 70:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")
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
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()