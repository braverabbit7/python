keys =["key1", "key2", "key3", "ddadawd"]
values = [1, 6, 3, 7]

a = {
    keys[index]: values[index]
    for index in range(0, len(values))
}
#print(a)


#Написать через цикл for +-

a ={}
for index, key in enumerate(keys):

    a[key] = values[index]

print(a)
