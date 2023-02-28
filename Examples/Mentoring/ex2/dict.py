#dict - словарь можем обращаться по имени к элементу
country = {4: 3}
#ключ: значение
print(country[4])

country = {"code": "Ru", "name": "Russian", "population": 144}
#Обращаемся по ключу с именем name
print(country["name"])
#используем dict
country2 = dict(code="ru", name="Russian", )
print(country2["code"])
#print(country2.items())

print("_______________")
#Доступ к ключам и значениям
for el , value in country.items():
    print(el, "-", value)
print("Обновить занчение словаря")
country['code'] = 'none'
print(country)

print("_______________")
#Очистить элемент словаря метод pop popitem (удалить последний элемент)
country.pop("name")
print(country)
#Очистить словарь
country.clear()
print(country)

#Если большая вложенность , словарь в словаре
person = {
    "user1" : {
        "first_name" : "Bob",
        "last_name" : "Marley",
        "age" : 30,
        "adress" : ("SPb", "Nevsky", "30"),
        (1,2, ): 30

    }
}
if person.get("user2") != None:

    print(person["user2"][(1, )]),
else:
    print("not found")