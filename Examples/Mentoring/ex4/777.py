numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
un_num=[]
for number in numbers:
    if number not in un_num:
        un_num.append(number)
print(un_num)