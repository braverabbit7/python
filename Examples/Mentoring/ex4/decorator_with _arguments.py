#Декораторы функций с параметрами
import time

def lim_requests(seconds):
#Простой декоратор со sleep (обернем сверху еще , чтобы передавать время)
    def lim_requests_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args,**kwargs)
            time.sleep(seconds)
            return res
        return wrapper
    return lim_requests_decorator
#Функцияя возврвщающая Hi there
@lim_requests(2)
def simple():
    return "Hi there"

print(simple())