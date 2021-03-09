def frequent_words(filename, word):
    """Подсчитывает количество частых слов в тексте"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filenames = ['paid_off.txt', 'adam_smith.txt']
for filename in filenames:
    frequent_words(filename, 'the')

# более подробная инфа про f строки https://shultais.education/blog/python-f-strings