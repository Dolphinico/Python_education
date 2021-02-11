class User():
    """Простая модель пользователя"""
    def __init__(self, first_name, last_name, location, profession):
        """Инициализация атрибутов имени"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.profession = profession
        self.login_attempts = 0
    def describe_user(self):
        """Описывает пользователя"""
        introduction = self.first_name.title() + ' ' + self.last_name.title() + ' is living in ' + self.location.title() + ' working as ' + self.profession.title()
        return introduction
    def info_login_attempts(self):
        """Описывает количество попыток залогитися"""
        print('This user ' + self.first_name.title() + ' ' + self.last_name.title() 
            + ' tryed to log in ' + str(self.login_attempts) + ' times.')
    def increment_login_attempts(self):
        """Увеличивает инфо о попытках залогинится на 1"""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Обнуляет количество попыток входа"""
        self.login_attempts = 0

n = User('dan', 'leo', 'perm', 'coder')
print(n.describe_user())

n.info_login_attempts()

n.increment_login_attempts()
n.increment_login_attempts()
n.increment_login_attempts()
n.increment_login_attempts()
n.info_login_attempts()

n.reset_login_attempts()
n.info_login_attempts()







