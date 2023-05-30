#Исключение 
x= input("x: ")
y= input("y: ")

try:
    x = int(x)
    y = int(y)
    res = x/y
except ZeroDivisionError:
    res = "Деление на ноль"
except ValueError:
    res = "Не числовое значение"

else:
    print("Исключений не произошло ",res)
finally:
    print("Блок finally выполняется всегда")
print(res)