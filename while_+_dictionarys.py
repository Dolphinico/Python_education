print('\nИспользование цикла while со словарями и списками')

#пример на списке пользователей, которые недавно зарегестрировались, но еще не были проверены

# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.

unconfirmed_users = ['alice', 'brain', 'jora']
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

# Вывод всех проверенных пользователей.

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())