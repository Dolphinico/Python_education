from user_modul import Admin

new = Admin("1111", "2222", "3333", '44444')
print(new.describe_user())
new.privileges.show_privileges()