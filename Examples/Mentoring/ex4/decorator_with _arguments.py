#Декораторы функций с параметрами
def func_decorator(func):
    def wrapper(x, *args, **kwargs):
        dx = 0.0001
        res = ()
