#Декораторы функций с параметрами
import time

def lim_requests(seconds): #в эту футнкцию передаем значение времени @lim_requests(х) где х- время задержки в секундах
#Простой декоратор со sleep (обернем сверху еще , чтобы передавать время)
    def lim_requests_decorator(func):
        def wrapper():
            res = func()
            time.sleep(seconds)
            return res
        return wrapper
    return lim_requests_decorator
#Функцияя возврвщающая Hi there
#@lim_requests(2)  #вызов декоратора с переменной 2
def simple(a):
    return "Hi there"
print(lim_requests(2),simple(), (2))