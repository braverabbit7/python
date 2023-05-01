# Сортировка строки
s2= [3, 2, 1, 4]
print(sorted(s2))

#Сортировака наоборот
print(sorted(s2, reverse=True))

d1={2: 'red', 1: 'green', 3: 'blue'}
# Вернется список отсортированных ключей
print(sorted(d1))   # Вывод:[1, 2, 3]

# Вернется список отсортированных значений
print(sorted(d1.values()))   # Вывод:['blue', 'green', 'red']