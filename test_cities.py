import unittest
from city_functions import get_city_name

class City_Names_Test(unittest.TestCase):
    """Тестирует возврат отформатированного имени в city_functions.py"""
    def test_country_city_names(self):
        """Проверка на правильный возврат отформатированного имени"""
        sorted_name = get_city_name('russia', 'perm')
        self.assertEqual(sorted_name, 'Russia Perm')
    
    def test_county_city_population(self):
        """Проверяет вызов функции"""
        sorted_name = get_city_name('santiago', 'chile','population=5000000')
        self.assertEqual(sorted_name, 'Santiago Chile Population=5000000')

unittest.main()
