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
