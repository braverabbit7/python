#map (func , *itarables)
a=[-1, 2, -6, -20, 9, 0]
b= list(map(abs,a))
print(b)
def func(x):
    return x**2

c=list(map(lambda x:x**2, a))
print(c)


print(list(map(str, a)))


