print("Найти минимальное значение списка с помошью if")
nums1 = [6, 3, 6, 7, 1, 4, 3]
nums2 = [6.4, 3.3, 6.2, 7.1, 1.4, 4.5, 3.1]

min = nums1[0]

for el in nums1:
    if  el < min:
        min = el

print(min)

print("Функция для поиска минимального числа:")
def minimal(l):
    min_num = l[0]
    for el in l:
        if el < min_num:
            min_num = el
    print(min_num)
minimal(nums1)
minimal(nums2)

