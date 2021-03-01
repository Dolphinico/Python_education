from user_modul_3 import User

class Privileges():
    """Описывает привелегии пользователя"""
    def __init__(self, privileges = ''):
        """Инициализирует атрибуты привелегий пользователя"""
        self.privileges = privileges
    def show_privileges(self):
        """Выводит список привелегий администратора"""
        priv = ['добавлять сообщения', 'удалять сообщения', 
                        'банить пользователей', 'удалять ползьвателей']
        for privs in priv:
            print('Admin allowed to ' + privs)

class Admin(User):
    """Модель администратора сайта"""
    def __init__(self, first_name, last_name, location, profession):
        """Инициализирует атрибуты администратора"""
        super().__init__(first_name, last_name, location, profession)
        self.privileges = Privileges()