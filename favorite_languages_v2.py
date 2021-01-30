favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'], 
'phil': ['python', 'haskell'],
} 
#В цикле for словаря создается другой цикл для перебора
#списка языков, связанных с каждым участником:
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name.title() + "'s favorite language is ")
    else:
        print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())
    