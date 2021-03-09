filename = 'i_love_programming.txt'

print("Enter 'quit' when you are finished.")
while True:
    ppl = input("\nWhy do you like to code? ")
    if ppl == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(ppl + "\n")
        print("Thank you, for your responce.")