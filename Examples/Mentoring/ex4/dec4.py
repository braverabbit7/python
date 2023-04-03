def mul(m):
    def dec(func):
        def wrapper(*args):


            return func(*args)*m

        return wrapper
    return dec


@mul(2)
def func(*args):


    return sum(args)


print(func(1,2,3,4,6))