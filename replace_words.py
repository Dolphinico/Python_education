print('\nЗамена отдельных слов в файле:\n')

filename = ('text_files/example_text.txt')
with open (filename) as file_object:
    contents = file_object.read()
    print(contents.replace('Python','C'))