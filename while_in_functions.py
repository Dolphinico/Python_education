print('\nИспользование функции в цикле while\n')

def get_formatted_name_4(first_name, last_name):
    """Возвращает аккуратно отформатированное имя"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# здесь вступает цикл while + input

while True:
    print('\nPlease tell me your name:')
# что бы цикл не был бесконечным, нужно дать пользователю возможность завершить программу - break:
    print("(enter 'q' at any time to quit)")
    f_name = input('Frist name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name =='q':
        break
    formatted_name = get_formatted_name_4(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')