countrys = ["Canada","Irlande","America","Japan","UK"]
print(countrys)#не отсортирован
countrys = ["Canada","Irlande","America","Japan","UK"]
print(sorted(countrys)) #отсортирован в алф. порядке
print(countrys)#не отсортирован
#обратная сортировка методом sorted() производится так:
countrys = ["Canada","Irlande","America","Japan","UK"] 
a = sorted(countrys, reverse=True) #отсортирован в обратном алфавитном порядке
print(a)
print(countrys)#не отсортирован
#сортировка методом reverse()
countrys = ["Canada","Irlande","America","Japan","UK"]
countrys.reverse() #обратный порядок сортировки, не в алф. порядке
print(countrys)
#возвращение списка в исходное состояние методом reverse()
countrys.reverse()
print(countrys)
#сортировка в алф. порядке методом sort()
countrys.sort()
print(countrys)
#сортировка в обратом алф. порядке методом sort()
countrys.sort(reverse = True)
print(countrys)
