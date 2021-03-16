import unittest

from class_employee import Employee

class TestEmployee(unittest.TestCase):
    """Тест модуля class_employee."""

    def setUp(self):
        """проверка создания модели работника."""
        self.eric = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        """Проверяет правильность работы увеличения зарплаты."""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """Проверка правильного кастомной зарплаты."""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

if __name__ == '__main__':
    unittest.main()