print('\nФлаги, для сложных программ с несколькими условиями\n')
#Если программа должна выполняться только при истинности нескольких условий,
#определите одну переменную - флаг, Эта переменная сообщает, должна ли программа выполняться далее

#пример работы флага на программе user_exit_programm.py

quick = "\nTell me something, and I will repeat it back to you:"
quick += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(quick)
    if message == 'quit':
        active = False
    else:
        print(message)