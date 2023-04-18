def func_decoraator(func):
    def wrapper():
        print("--Before--")
        func()
        print("--After--")
    return wrapper

def some_func():
    print("Some_func")
some_func = func_decoraator(some_func)

some_func()
