def mul(m):
    def dec(func):
        def wrapper(*args):
            return func(*args)*m

        return wrapper
    return dec


@mul(2)
def func1(*args):
    return sum(args)


print(func1(1, 2, 3, 4, 6))


