s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6, 6])

#Обьеденить
print(s2.union(s1))
#Общие элементы
print(s2.intersection(s1))
#Разница
print(s1.difference(s2),  s2.difference(s1))