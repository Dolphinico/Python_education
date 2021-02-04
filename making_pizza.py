import pizza

pizza.making_pizzas('12', 'pepperoni')
pizza.making_pizzas('23', 'cheese','beef','pork')

# В процессе обработки этого файла строка import pizza 
# приказывает Python открыть файл pizza.py и скопировать все функции из него в программу

# Если ограничиться импортированием только той функции, которую хотите использовать, 
# пример making_pizzas py будет выглядеть так:
from pizza import making_pizzas

making_pizzas(16, 'pepperoni')
making_pizzas(12, 'mushrooms', 'green peppers', 'extra cheese')

# если функция находится не рядом с модулем водной дериктории, программа не сработает