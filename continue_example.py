#продолжить работу цикла, не переписывая код заново, можно воспользоваться командой continue для возвращения
#к началу цикла и проверке условия

#пример на цикле отсчета с 1 до 10:

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: #все что кратное 2, программа пропускает, но не останавливается
        continue
    print(current_number)

#Предотвращение зацикливания:

print('\nПредотвращение зацикливания\n')

x = 1

while x <= 5: 
    print(x)
    x += 1 #эта строчка не дает циклу повторяться бесконечно, программа останавливается по достижению числа 5

#если забыть добавить эту строчку, то цикл будет выполнятся бесконечно, конкретно в данном случае будет выводится только 1
