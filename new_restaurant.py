class New_r():
    """Простая модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type):
        """"Инициализирует имя ресторана, тип кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Описывает ресторан"""
        r_info = self.restaurant_name.title() + " is opened and greetings  you!" + '\n' + 'We can cook in different styles: ' + self.cuisine_type.title()
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
    
r = New_r('restaurant', 'russian, englang, american, itally.')
print(r.describe_restaurant())

r.set_number_served(10)
r.update_served_numbers()

r.increment_number_served(20)
r.update_served_numbers()

