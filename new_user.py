class User():
    """Простая модель пользователя"""
    def __init__(self, first_name, last_name, location, profession):
        """Инициализация атрибутов имени"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.profession = profession
    def describe_user(self):
        """Описывает пользователя"""
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.location.title()) 
        print(self.profession.title())
    def greet_user(self):
        """Персональное приветствие"""
        print("Lets welcome " + self.first_name.title() + " " + self.last_name.title() + "!")
        print('Here is some information about him: \n')

a = User('daniil', 'leontev', 'polazna', 'programmer')
a.greet_user()
print("His name is " + a.first_name.title() + " " + a.last_name.title() + ".")
print("He lives in " + a.location.title() + ".")
print("And  he works as "  + a.profession.title() + ".\n")

b = User('alexandr', 'sokolov', 'polazna', 'QA tester' )
b.greet_user()
print("His name is " + b.first_name.title() + " " + b.last_name.title() + ".")
print("He lives in " + b.location.title() + ".")
print("And  he works as "  + b.profession.title() + ".")
