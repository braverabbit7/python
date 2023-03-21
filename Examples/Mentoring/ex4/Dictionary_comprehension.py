print("List comprehension ")
a = [i for i in range(1, 11)]
print(a)
print("Возвести в квадрат")
a = [i**2 for i in range(1, 11)]
print(a)

######-------

print("Dict comprehension")
#Словарь изсебя представляет структуру Key:value
print("Возведем значение key в квадрат")
a = {i:i**2 for i in range(1, 11)}
print(a)

print("Подсчет букв в словах")
a = {word: len(word) for word in ["hello", "hi", "sometext"]}
print(a)

print("Пример переделывания списка в словарь")
users = [
    [0, "Joe", "pass"],
    [1, "Martin", "123"],
    [2, "Rick", "key"],
    [54, "David", "smth"],
]
print(users[3])
#Делаем так, чтобы к пользователю можно было обращаться с помошью id
new_users = {user[0]:user for user in users}
print(new_users[54])

print("Еще пример с генератором словарей")
m = {"Неуд":2, "уДовЛ":3, "Хор":'4',"отЛ":'5'}
print("Вывод до преобразования:", m)
#Предобразум в словарь Все буквы-заглавные, все занчения в числа
a = {key.upper(): int(value) for key, value in m.items()}
print("Вывод после преобразования:", a)