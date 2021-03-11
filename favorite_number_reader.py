import json
filename = 'favorite_number.json'

with open(filename) as file_object:
    usernumber = json.load(file_object)
    
    print("I know your favorite number! " + " The number is " + usernumber + "!")