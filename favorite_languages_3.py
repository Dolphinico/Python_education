from collections import OrderedDict
favorite_languages = OrderedDict() 
# Обратите внимание на отсутствие фигурных скобок; вызов OrderedDict() создает пустой упорядоченный словарь
# и сохраняет его в favorite_languages. Затем пары из имени и языка последовательно добавляются в словарь.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby', 
'phil': 'python'
} 

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " + language.title() + '.')

# Теперь при переборе favorite_languages при выполнении цикла for, данные всегда будут выдаваться
# в порядке их добавления.

# Это чрезвычайно полезный класс, объединяющий основное преимущество списков
# (сохранение исходного порядка) с главной особенностью словарей (связывание
# двух видов информации).
