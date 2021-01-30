#Большое количество пользователей(пример)
#Словарь в словаре на примере словаря пользователей
print('\nСловарь в словаре на примере словаря пользователей\n')

users = {
    'aenstein': {
        'first': 'albert',
        'second': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'second': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location'] 
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())