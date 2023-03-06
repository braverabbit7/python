# Локальные имена
#Правило по которому python ищет переменню или функцию
# Определение имен за пределами функции - глобальные переменные
a = 'Hello world!' # Имя a, которое является строкой
b = [ 2, 3, 8.55, 'Textbook' ] # Имя b, которое является списком

# Определение имен внутри функции
def Fn():
    a = 2.777 # имя a - число с плавающей точкой
    b = { 1:'One', 2:'Two' } # имя b - словарь
    c = [ 0.1, 0.01, 0.001 ] # имя c - список
    print('Fn.a = ', a)
    print('Fn.b = ', b)
    print('Fn.c = ', c)

# Вывести имена, которые объявлены за пределами функции
print('a = ', a)
print('b = ', b)

# Вызвать функцию
Fn()