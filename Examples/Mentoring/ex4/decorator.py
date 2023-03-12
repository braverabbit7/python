a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
database = []
i = 0

def decorator(func):
    def wrapper(*args, **kwargs):


        print("Код до выполнения:")
        database.extend([a, b])
        print(database)
        print("Код после выполнения:")
        func()
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