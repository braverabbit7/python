#Есть встроеные , а можно создовать свои def название_функции(передаваемый параметр)
def test_func():
#Передаем что делает функция
    print("Hello", end="")
    print("!")
#Вызываем саму функцию
test_func()


print("Передаем значение в функцию")

def test_func2(w):
    print(w, end="")
    print("!")


test_func2("Hi")
test_func2(7)
test_func2(7.6)

print("Еще пример--------------------------(складывание строк и чисел)")
def sum(a, b):
    res = a + b
    print("Result:", res)
a1 = int(input("Введите число a:"))
a2 = int(input("Введите число b:"))
sum(a1, a2)
b1 = str(a1)
b2 = str(a2)
sum(b1, b2)

print("Если надо вернуть знвчение функции return(Вщзвращаем res))")

def sum2(a, b):
    res = a + b
    return res
#Можно сократить используя return a+b
res = sum2(a1, a2)
print(res)


