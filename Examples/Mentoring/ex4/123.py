print("For")
array = [1, 2, 3, 4, 5]
for i in range(len(array)):
    array[i] = array[i]+1
print(array)

print("While")
array = [1, 2, 3, 4, 5]
l = 0
while l < len(array):
   array[l] = array[l]+1
   l += 1
print(array)

print("List comprehension")
array = [1, 2, 3, 4, 5]
array = [a+1 for a in array]
print(array)