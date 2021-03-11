from name_function import get_formatted_name

print("Enter 'q' at any time to quit")
while True:
    first = input("\nGive me a first name please ")
    if first == 'q':
        break
    last = input("Give me a last name please ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print('\tNeatly formatted name: ' + formatted_name + '.')