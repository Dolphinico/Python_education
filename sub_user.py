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
class Admin(User):
    """Модель администратора сайта"""
    def __init__(self, first_name, last_name, location, profession):
        """Инициализирует атрибуты администратора"""
        super().__init__(first_name, last_name, location, profession)
        self.privileges = ['добавлять сообщения', 'удалять сообщения', 
                        'банить пользователей', 'удалять ползьвателей']
    def show_privileges(self):
        """Выводит список привелегий администратора"""
        for privileges in self.privileges:
            print('Admin allowed to ' + privileges.title())


a = Admin('dan','leo','prm','prgrm')
a.show_privileges()






