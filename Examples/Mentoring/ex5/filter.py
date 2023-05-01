#filter (Function or none, itrable)
a = [10,2,3,4,11,23,44,55]
b = list(filter(lambda x: x > 10, a))
print(b)