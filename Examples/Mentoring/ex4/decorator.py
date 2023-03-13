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


@decorator
def show():
    return a + b

show()
#Можно вместо @decorator использовать так
#dec = decorator (show)
#dec()