keys =["key1", "key2", "key3"]
values = [1, 2, 3]

a = {
    keys[index]: values[index]
    for index in range(0, len(values))
}
print(a)