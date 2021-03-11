import json

usernumber = input('What is your favorite number? ')
filename = 'favorite_number.json'

with open(filename, 'w') as file_object:
    json.dump(usernumber, file_object)
    print("Thank you!")