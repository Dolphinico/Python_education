mes = "Введите возраст посетителя кинотеатра: "
message = ""
while mes != 'quit':
    message = int(input(mes))
    if message <= 3:
        print("Билет бесплатный")
    elif message <= 12:
        print("Билет стоит 10 долларов")
    elif message > 12:
        print("Билет стоит 15 долларов")
