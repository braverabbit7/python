print("-----------Map------------")
print("Для каждого элемента списка применяем функцию abs(по модулю):")
a = [1, 2, -3, 4, -5, 6]
print(list(map(abs, a)))


print("Умножим каждый элемент списка на x2:")
#создадим функцию f(x) где умножаем на 2 каждый элемент
def f(x):
    return (x*2)
#Обьявим список и применим к каждому элементу списка map
a = [1, 2, 3, 4, 5, 6]
print(list(map(f, a)))

print("-----------Filter------------")