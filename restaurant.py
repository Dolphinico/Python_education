# Ресторан: создайте класс с именем Restaurant 
# Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type 
# Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), 
# который выводит сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant.
# Выведите два атрибута по отдельности, затем вызовите оба метода.

class Restaurant():
    """Простая модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type):
        """"Инициализирует имя ресторана, тип кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Описывает ресторан"""
        print(self.restaurant_name.title() + " is always welcome to you")
        print(self.cuisine_type)
    def open_restaurant(self):
        """Выводит информацию о состоянии ресторана"""
        print("Now the " + self.restaurant_name.title() + " is opened!")

rest = Restaurant("moe's", "home made")
rest.open_restaurant()
print("Welcome to " + rest.restaurant_name.title())
print("All of our cuisine is " + rest.cuisine_type + ".\n")

new_rest = Restaurant('joe','spain')
new_rest.open_restaurant()
print("Welcome to " + new_rest.restaurant_name.title())
print("All of our cuisine is " + new_rest.cuisine_type.title() + ".")




        