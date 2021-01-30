#Содержательные подсказки
#name = input('Please print your name: ')
#print('Hello ' + name +'!')

#для отображения подсказки более чем в одну строку можно сохранить ее в переменной и передать переменную в input()
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '
#Первая часть длинного сообщения сохраняется в переменной prompt. Затем оператор += объединяет текст, хранящийся в prompt
name = input(prompt)
print('Hello ' + name + '!')