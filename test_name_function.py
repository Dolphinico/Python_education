# Ниже приведен тестовый сценарий с одним методом, который проверяет,
# что функция get_formatted_name() правильно работает при передаче имени и фамилии:

import unittest

from name_function import get_formatted_name
# создается класс NamesTestCase, который содержит серию модульных тестов для get_formatted_name().
# Имя класса выбирается произвольно, но лучше выбрать имя, связанное с функцией:

# Этот класс должен наследовать от класса unittest.
# TestCase, чтобы Python знал, как запустить написанные вами тесты.

# В тестовом методе вызывается тестируемая функция и сохраняется возвращаемое значение,
# которое необходимо проверить.
# В данном примере вызывается функция get_formatted_name() с аргументами 'janis' и 'joplin',
# а результат сохраняется в переменной formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py"""

    def test_first_last_names(self):
        """Имена вида 'Janis Joplin' в одной строке работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
# здесь используется одна из самых полезных особенностей unittest: метод
# assert. Методы assert проверяют, что полученный результат соответствует тому
# результату, который вы рассчитывали получить:
        self.assertEqual(formatted_name, 'Janis Joplin')
# Имя метода должно начинаться с test_, чтобы этот метод выполнялся автоматически при запуске
# test_name_function.py.
        def test_first_middle_last_names(self):
                """Работают ли такие имена, как 'Wolfgang Amadeus Mozart'?"""
                formatted_name= get_formatted_name(
                        'wolfgang', 'amadeus', 'mozart')
                self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

