print('Упражнение 11-1\n')

# Город, страна: напишите функцию, которая получает два параметра: название страны и название города
# Функция должна возвращать одну строку в формате «Город, Страна», например «Santiago, Chile»
# Сохраните функцию в модуле с именем city_functions.py
# Создайте файл test_cities py для тестирования только что написанной функции (не забудьте
# импортировать unittest и тестируемую функцию)
# Напишите метод test_city_country() для проверки того,
# что вызов функции с такими значениями, как ‘santiago’ и ‘chile’, дает правильную строку.
# Запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.

# задача выполнена в city_functions.py + city_name.py + test_cities.py

print('\nУпражнение 11-1\n')

# Население: измените свою функцию так, чтобы у нее был третий обязательный параметр — население.
# В новой версии функция должна возвращать одну строку вида «Santiago, Chile — population 5000000 » 
# Снова запустите программу test_cities.py
# Убедитесь в том, что тест test_city_country() на этот раз не проходит.
# Измените функцию так, чтобы параметр населения стал необязательным.
# Снова запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
# Напишите второй тест test_city_country_population(), который проверяет вызов функции
# со значениями ‘santiago’, ‘chile’ и ‘population=5000000’.
# Снова запустите test_cities py и убедитесь в том, что новый тест проходит успешно.

# city_functions.py + city_name.py + test_cities.py