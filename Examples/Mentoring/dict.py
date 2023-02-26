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
print(country2.items())