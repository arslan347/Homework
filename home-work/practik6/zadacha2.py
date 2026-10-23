number = int(input("Номер вашего кармана: "))

#если число входит в заданный диапозон
if number < 0 or number > 36:
    print("ошибка ввода")

#0 - зеленый карман
elif number == 0:
    print("зеленый")

#цвета карманов 0-10
elif 1 <= number <= 10:
    if number % 2 == 0:
        print("черный")
    else:
        print("красный")

#цвета карманов 11-18
elif 11 <= number <= 18:
    if number % 2 == 0:
        print("красный")
    else:
        print("черный")

#цвета карманов 19-28
elif 19 <= number <= 28:
    if number % 2 == 0:
        print("черный")
    else:
        print("красный")

#цвета карманов 29-36
else:
    if number % 2 == 0:
        print("красный")
    else:
        print("черный")
