print("Создание list с 1 до 5")
nums = [n for n in range(1,6)]
print(nums)

print("Умнодение каждого элемента на самого себя")
nums = [1, 2, 3, 4, 5]
squares = [n*n for n in nums]
print(squares)

print("Проверка с if(только не четные)")
nums = [1, 2, 3, 4, 5]
odd_squares = [n*n for n in nums if n%2 == 1]
print(odd_squares)