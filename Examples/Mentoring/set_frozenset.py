#Зададим обычный list
a = [4, 6, 6, 7, 6, 8]
print(a)
print("Удалить все повторения")
print(set(a))
#set add множество set обозначается в {}
b = {4, 5}
print(b)
b.add(44)
print(b)
#update set функция set выстраивает все рандомом
b.update(['44', True, 4.5])
print(b)
#удалить 1 й элемент метод pop
b.pop()
print(b)
#Очистить множество
b.clear()
print(b)
print("__________________")
#Frozenset - не изменяемый кортедж set
a_n = frozenset(a)
print(a_n)
#нельзя обратиться к элементу кортеджа a_n.add(44)