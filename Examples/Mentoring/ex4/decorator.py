a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
def decorator(func):
    def wrapper(*args, **kwargs):

        database = []
        database.extend([a, b])
        print("Код до выполнения:", database)

        func()

        print("Код после выполнения:", func(*args, **kwargs))

    return wrapper

def intcheck(func):
    def wrapper1():
        print("a", type(a))
        func()
        print("b", type(b))

    return wrapper1


@decorator
#@intcheck
def show():

    return "Сложение", a + b

show()

@decorator
def show1():

   return "Умножение", a * b

show1()
#Можно вместо @decorator использовать так
#dec = decorator (show)
#dec()