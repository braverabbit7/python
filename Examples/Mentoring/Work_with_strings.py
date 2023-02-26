# Вывод на несколько строк тройные кавычки
print("""fdaffafwa
afdwafaf
afawafa""")
# Перевод на след строку \n
print("Привет \n мир")
#\t табуляция
print("\t привет \n \t мир")
#Печать с""
print("'привет'")

#Экранирование
print("Привет \"в\" кавычках")

#Сложение строк (конкостинация)
a = "привет"
b = "мир"
print(a + " " + b)

#Вывод определенного символа
print(a[0])
#Срез
print(b[0:2])
#Методы написания строк
print(a.upper())
print(b.lower())
print(a.capitalize())
#переводим текст в список
txt = "привет мир куда идешь"
print(txt.split(" "))
#Список в строчку перевод через /
list1 = ["a", "b", "c"]
print("/".join(list1))

#удаление пробелов вначале и вконце
txt = "    sdhgnidgns    12isjgnsgni   "
print(txt.strip())

# Замена символов строке заменяем l на о
txt = "olololololololo"
print(txt.replace("l", "o"))