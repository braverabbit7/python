#
def func(*args):
    print(args)

func(3, 5, 6)



print("Чтобы сделать кортеджем сложение добавляем в func2(*l) * для перевода из котреджа")

def func2(*args):
    print(args)
    print(sum(args))
l = [1, 2, 3]
func2(*l)

print("Добавим позиионный аргумент a в def func3(a, *args). Первый элемент попадает в а =1:")

def func3(a, *args):
    print(a)
    print(args)
    print(sum(args))
l = [1, 2, 3]
func3(*l)

print("**Kwargs ** -означает упаковку в словарь kwargs - key world agreements")

def func4(*args, **kwargs):
    print(args)
    print(kwargs)
l = [1, 2, 3]
func4(l)