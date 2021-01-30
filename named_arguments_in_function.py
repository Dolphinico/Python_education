print('Именованные аргументы\n')

def describe_pet(animal_type, pet_name):
    """Выводит сообщение о животном"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name.title() + '.')
describe_pet(animal_type='dog', pet_name='dogg')

# Функция не меняется, но в этот раз python 100% понимает что animal_type это dog, а pet_name это dogg
# В данном случае порядок следования аргументов не важен, тк они уже определены