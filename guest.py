greetings = input("Hello, whats your name? ")
print("Nice to meet you " + greetings)

filename = 'guest.txt'

with open (filename,'w') as file_object:
    file_object.write(greetings)