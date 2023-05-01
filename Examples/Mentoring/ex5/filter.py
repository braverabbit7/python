#filter (Function or none, itrable)
def f (x):
    return x>10

a = [10,2,3,4,11,23,44,55]
b = list(filter(f,a))
print(b)