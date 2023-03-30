def decor(func):
    def wrapper(a, b):
        print("_________")
        a = func(a, b)
        print(a)
        print("_________")

        return a
    return wrapper

def simpe(a, b):
    return a+b


simpe = decor(simpe)
simpe(1, 2)
