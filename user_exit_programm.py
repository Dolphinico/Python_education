print('\nПример завершения работы пользователем')

quick = "\nTell me something, and i'll repeat it back to you:"
quick += "\nEnter 'quit' to end the programm. "
message = ""
while message != 'quit':
    message = input(quick)
    if message != 'quit':
        print(message)

#что бы при в вводе quit сообщение не дублировалось, а выполнялась команда, можно добавить простую проверку if