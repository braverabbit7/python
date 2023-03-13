a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
def decorator(func):
    def wrapper(*args):

        database = []
        database.extend([a, b])
        print("Код до выполнения:", database)

        func()

        print("Код после выполнения:", func(*args))

    return wrapper

def intcheck(show):
    def wrapper1():
        print(type(a))
        show()
        print(type(b))

    return wrapper1


@decorator
#@intcheck
def show():
    return a + b

show()

@decorator
def show1():
    return a - b

show1()
#Можно вместо @decorator использовать так
#dec = decorator (show)
#dec()