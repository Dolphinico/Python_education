# Функция get_formatted_name() строит полное имя из имени и фамилии, разделив их пробелом,
# преобразует первый символ каждого слова к верхнему регистру и возвращает полученный результат:

# def get_formatted_name(first, last):
#     """Строит отформатированное полное имя."""
#     full_name = first + ' ' + last
#     return full_name.title()

# для тестирования что программа работает правильно,
#создаем еще одну программу, которая протестирует эту - names.py


def get_formatted_name(first, last, middle = ''):
    """Строит отформатированное полное имя."""
    full_name = first + ' ' + middle + last
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

