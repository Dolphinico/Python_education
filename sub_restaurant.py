class New_r():
    """Простая модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type):
        """"Инициализирует имя ресторана, тип кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Описывает ресторан"""
        r_info = self.restaurant_name.title() + " is opened and greetings you!" + '\n' + 'We can cook in different styles: ' + self.cuisine_type.title()
        return r_info
    def set_number_served(self, number):
        """Задает количество обслуженных посетителей"""
        self.number_served = number
    def update_served_numbers(self):
        """Выводит информацию о количестве обслуженых столов"""
        print('Today we are served ' + str(self.number_served) + ' customers!')
    def increment_number_served(self, customer):
        """Увеличивает число обслуженных посетителей"""
        self.number_served += customer

class IceCreamStand(New_r):
    """Выводин информацию о стенде с мороженным"""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты субкласса"""
        super().__init__(restaurant_name, cuisine_type)
        self.ice_flavors = 'qwerty flavored ice cream'
    def describe_flavors(self):
        """Описывает вкусы мороженного"""
        print("We have " + self.ice_flavors + '.')
        

r_ice = New_r('jjjjj', 'qqqqq')
print(r_ice.describe_restaurant())
r_ice.set_number_served(10)
r_ice.update_served_numbers()

r_ice.increment_number_served(20)
r_ice.update_served_numbers()

r_ice = IceCreamStand('qwerty','yuiop')
r_ice.describe_flavors()
