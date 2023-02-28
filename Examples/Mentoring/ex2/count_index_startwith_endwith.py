#Метод index() в Python помогает найти значение индекса элемента в последовательности.
#Он выдает наименьший возможный индекс указанного элемента.
#Если указанный элемент не существует, то возвращается ValueError.


x = 'количество вхождений подстроки `sub` в диапазоне индексов'
print(x.count('и'))

#Index. Находит первре вхждение
a = 'Just simple text'
print(a.index('t'))
#Указываем после какого символа ищем вхождение
print(a.index('t', 4))

#Startwith
#Метод str.startswith() возвращает True, если строка str начинается указанным префиксом prefix,
# в противном случае возвращает False.
print("Startwith")
x = 'начинается указанным префиксом prefix'
print(x.startswith('начина'))
print(x.startswith('указанным'))
#С 11 символа
print(x.startswith('указанным',11))
#Endwith
print("Endwith")
str = 'Быть или не быть, вот в чём вопрос.'

print(str.endswith('вопрос.'))   # true
print(str.endswith('быть'))     # false
print(str.endswith('быть', -23)) # true ??? не возвращает

