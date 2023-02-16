#!/usr/bin/env python
# -*- coding: utf-8  -*-
call = int(input("Количество дневных калорий:"))
brekfast = int(input("Колории на завтрак:"))
lanch = int(input("Колории на обед:"))
dinner = int(input("Колории ужин:"))
banana = (50)
nuts = (100)
raisin = (200)
total_cal = (brekfast+lanch+dinner)
calories_left = int(call - total_cal)
if call > total_cal:
    print("Можно докушать на ",calories_left, "калорий")
    if calories_left > banana:
        nuts_left = (int(calories_left) / int(nuts))
        banana_left = (int(calories_left) // int(banana))
        raisin_left = (int(calories_left)/ int(raisin))

        print("Можете сьесть ", nuts_left," кг орешков или", banana_left, "бананов или", raisin_left,"килограмм изюма")
    else:
        print("Всего", calories_left, " калорий осталось,даже банан не сьесть . Лучше водички и спать")
else:
    print ("Пережер на ", abs(calories_left), "калорий")