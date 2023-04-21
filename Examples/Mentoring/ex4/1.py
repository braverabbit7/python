a = 1
def foo():
    global a
    a = 2
    def bar():
        global a
        a = 3

        print(a)

    bar()

    print(a)


foo()
print(a)