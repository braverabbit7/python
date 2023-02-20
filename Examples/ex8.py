import random
rabbit = ["Робби", "Вильямс", "Ватан", "Меркури", "Филя", "Матис"]
food = ["Морковь", "Капуста", "Брокколи", "Трава", "Картошка", "Яблоки"]

for i in range(0, len(rabbit)):
    print(rabbit[i], "-", random.choice(food))