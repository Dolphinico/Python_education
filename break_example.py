#пример работы команды break

#Чтобы прервать цикл while, программа выполняет команду break,
#как только пользователь введет значение 'quit':

quick = "\nPlease enter the name of a city uyou have visited:"
quick += "\n(Enter 'quit' when you are finished.) " 

while True:
    city = input(quick)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")