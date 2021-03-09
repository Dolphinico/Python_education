import json
# для чтения данных используется тот же файл, в который эти данные были записаны:
filename = 'numbers.json'
# конкретно в этом примере файл открывается в режиме чтения, потому что Python
# нужно только прочитать данные из файла:
with open(filename) as f_obj:
# функция json.load() используется для загрузки информации из numbers json;
# эта информация сохраняется в переменной numbers:
    numbers = json.load(f_obj)
print(numbers)