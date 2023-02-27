les = []
l = int(input('Количество предметов:'))
i = 0
while i < l:
    i += 1
    print("Введите ", i, " предмет:", end="")
    x = input()
    les.append(x)

print(les)