keys =["key1", "key2", "key3", "ddadawd"]
values = [1, 6, 3, 7]

a = {
    keys[index]: values[index]
    for index in range(0, len(values))
}
#print(a)


#Написать через цикл for +-

a ={}
index = 0
for i in values:

    a[keys[index]] = i
#    print(keys[index])
#    print(i)
    index += 1

print(a)




#b={}


#b[5] = 6
#b[7] = 8
#b[9] = 10

#print(b)