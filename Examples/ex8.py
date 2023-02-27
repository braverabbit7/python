import random
rabbit = ["Робби", "Вильямс", "Ватан", "Меркури", "Филя", "Матис"]
food = ["Морковь", "Капуста", "Брокколи", "Трава", "Картошка", "Яблоки"]
i = 0
while i in range(0, len(rabbit)):

    print(rabbit[i], "-", random.choice(food))
    i += 1