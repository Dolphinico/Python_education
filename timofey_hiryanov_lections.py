#небольшие полезные примеры из лекции:
print('\nнебольшие полезные примеры из лекции:\n')

def hello_n(name:str, n:int):
    """вывод приветствия, много раз"""
    for i in range(n):
        print('Привет', name.title())
hello_n('вася',5)

print('\n')

# небольшой пример работы с range()
A = range(1,6) 
print(*A)
print(A[4])
for x in A:
    print(x)
print('\n')


    