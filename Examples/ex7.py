import random
rabbit = ["Робби", "Вильямс", "Ватан", "Меркури", "Филя", "Матис"]
food = ["Морковь", "Капуста", "Брокколи", "Трава", "Картошка", "Яблоки"]

for i in rabbit:

    print(random.choice(rabbit), " - ",  random.choice(food) )

