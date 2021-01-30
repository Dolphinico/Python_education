print('Значения по умолчанию\n')

# в этом примере по умолчанию задается параметр animal_type = 'dog',
# python будет знать что по умолчанию стоит в этом параметре и теперь его не нужно прописывать еще раз при вызове функции

def describe_pet(pet_name, animal_type='dog'):
    """Выводит сообщение о животном"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name.title() + '.')

describe_pet(pet_name='dogg') #что бы вывести имя любого другого животного, функция будет вызываться так:
# describe_pet(animal_type='cat', pet_name='catt')