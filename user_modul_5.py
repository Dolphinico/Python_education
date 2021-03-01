from user_modul_3 import User
from user_modul_4 import Privileges, Admin

new = Admin("1111", "2222", "3333", '44444')
print(new.describe_user())
new.privileges.show_privileges()
