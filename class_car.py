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

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()