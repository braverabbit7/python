a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))


def decorator(func):
    def wrapper(*args):

        database = []

        print("Код до выполнения:")
        database.extend([a, b])
        print(database)
        func()
        print("Код после выполнения:")
        i = func(*args)
        print(i)


    return wrapper

@decorator
def show():

        return a + b

show()
#Можно вместо @decorator использовать так
#dec = decorator (show)
#dec()