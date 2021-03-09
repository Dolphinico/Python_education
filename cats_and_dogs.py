def cats_and_dogs (filename):

    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(contents)     
    except FileNotFoundError:
        pass
        # print("Sorry i can' find this file - " + filename)

# filepath = 'text_files/cats.txt'
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    cats_and_dogs(filename)
    