import json

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        usernumber = json.load(file_object)
except FileNotFoundError:
    usernumber = input("What is your favorite number? ")
    with open (filename, 'w') as file_object:
        json.dump(usernumber,file_object)
        print("Next time i will guess your number!")
else:
    print('I know your favorite number! ' + '\nThe number is - ' + usernumber)
        