def func(*args):
    l = [args[0] * n for n in args[1:]]
    print(l)

func(3, 4, 5)


