#Посчитаем время выполнения функции :
from datetime import datetime
def f():
    stat = datetime.now()
    l = []
    for i in range(20000):
        if i % 2 == 0:
            l.append(i)
    print(datetime.now() -stat)
    return l
l1 = f()

print(l1)

#Написание Декоратора

def timeit(func):
    def wrapper():
        start =datetime.now()
        result =func()
        print(datetime.now() - start)
        return result
    return wrapper


print("С декоратором")
@timeit
def f():
#    stat = datetime.now()
    l = []
    for i in range(20000):
        if i % 2 == 0:
            l.append(i)
#    print(datetime.now() -stat)
    return l


l1 = f()

print(l1)