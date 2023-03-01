s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6, 6])
c = []
for i in s1:
    for j in s2:
        if i == j:
            c.append(i)
            break
print(c)