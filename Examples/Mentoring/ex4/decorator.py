a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
database = []
i = 0
def decorator(func):
    def wrapper():


        print("Код до выполнения:")
        database.extend([a, b])
        print(database)
        print("Код после выполнения:")
        func()
        print(i)

    return wrapper

@decorator
def show():

    i = (a + b)

show()
#Можно вместо @decorator использовать так
#dec = decorator (show)
#dec()