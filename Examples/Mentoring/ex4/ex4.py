def dec(func):
    def wrapper(*args):
        print("before")
        n = func(*args)
        print("after")
        return n
    return wrapper

@dec
def fun1(a, b):
    return a+b

print(fun1(3, 4))


