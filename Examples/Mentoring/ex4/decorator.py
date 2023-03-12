def fib(x):
    d = fib(x-1) + fib(x-2) if x > 1 else x
    return d

print(fib(10))
