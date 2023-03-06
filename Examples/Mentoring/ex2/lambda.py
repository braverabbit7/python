#Лямбда-функции в Python являются анонимными.
# Это означает, что функция безымянна.
# Как известно, ключевое слов def используется в Python для определения обычной функции.
# В свою очередь, ключевое слово  lambda  используется для определения анонимной функции.
double = lambda x: x*2
print(double(5))



#____________________




def mul(f, i=2):

    return f(1, 2) * i

print(mul(lambda a, b: a + b))

