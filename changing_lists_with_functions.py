print('\nИзменение списка в функции\n')

# Если вы передаете список функции, код функции сможет изменить список. Все
# изменения, внесенные в список в теле функции, закрепляются, что позволяет эф-
# фективно работать со списком даже при больших объемах данных.

#пример реализации кода без использования функции, только цикл while, 
# на примере компании котороая печатает на 3D принтере:

# сначала мы создаем список деталей(которые принес заказчик):
unprinted_designs = ['iphone case', 'robot servant', 'little doll', 'mini car']
complited_models = []

# цикл while последовательно печатает каждую модель до конца списка.
# после печати каждая модель будет перемещена в новый список complited_models

while unprinted_designs:
    current_design = unprinted_designs.pop()
    # далее идет команда печати моделей:
    print('Printing model: ' + current_design)
    complited_models.append(current_design)

# а затем выводим список уже готовых деталей:
print("\nThe following models have been printed:")
for model in complited_models:
    print(model)

print('\nВерсия когда с использованием функции\n')
# теперь, меняем код в сторону функциональности, добавляем 2 функции, каждая будет решать свою задачу:

def print_models(unprinted_designs, complited_models): 
    # сначала определяется функция print_models() с двумя параметрами: список
    # моделей для печати и список готовых моделей. Функция имитирует печать каж-
    # дой модели, последовательно извлекая модели из первого списка и перемещая
    # их во второй список.
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # имитация печати модели на 3D принтере:
        print('Printing model: ' + current_design)
        complited_models.append(current_design)
    
def show_complited_models(complited_models):
    # здесь определяется функция show_completed_models()
    # с одним параметром: списком напечатанных моделей. Функция show_completed_
    # models() получает этот список и выводит имена всех напечатанных моделей.
    """Выводит информацию о всех напечатаных моделях"""
    print('\nThe follofing models have been printed:')
    for complited_model in complited_models:
        print(complited_model)

# сама программа:

unprinted_designs = ['iphone case', 'robot servant', 'little doll', 'mini car']
complited_models = []

print_models(unprinted_designs[:],complited_models)
show_complited_models(complited_models)

print('\nЗапрет изменения списка в функции\n')

# Иногда требуется предотвратить изменение списка в функции.
# допустим после печати всех моделей исходный список нужно оставить для отчетности. 
# Но, поскольку все имена моделей были перенесены из списка unprinted_designs, остался только
# пустой список; исходная версия списка потеряна.

# в таком случае, нужно передать функцию копии оригинального списка, 
# тогда все изменения будут применяться на копию, оригинал останется неизменным

# Чтобы передать функции копию списка, можно поступить так:
# имя_функции(имя_списка[:])

# Если удаление элементов из списка unprinted_designs в print_models py нежелательно, функцию
# print_models() можно вызвать так:

print_models(unprinted_designs[:], complited_models)
