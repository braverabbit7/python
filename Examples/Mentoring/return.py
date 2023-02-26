def rec(valve):
    print(valve)
    if valve < 4000:
        rec(valve+100)
    print(valve)
rec(1)
#глубина рекрсии 997
#Рекурсия- функция, которая вызыват сама себя

