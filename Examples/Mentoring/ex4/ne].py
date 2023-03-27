def decorator(func):
    def wrapper():
        res = func()
        return res
    return wrapper()


def sum1(a,b):
    return a+b

decorator(sum1)

print(sum1(1,2))
######-------Разобрать дома с 0 написать декратор

