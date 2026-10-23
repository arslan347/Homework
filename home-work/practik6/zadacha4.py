# вводим данные
vvod = input()
dannye = vvod.split()

# достаём числа
x1 = int(dannye[0])
y1 = int(dannye[1])
x2 = int(dannye[2])
y2 = int(dannye[3])

# если ошибка
oshibka = False

# проверяем координаты
if x1 < 1 or x1 > 8:
    oshibka = True
if y1 < 1 or y1 > 8:
    oshibka = True
if x2 < 1 or x2 > 8:
    oshibka = True
if y2 < 1 or y2 > 8:
    oshibka = True

# если ошибка
    print("ошибка ввода")
else:
    # проверяем не одна ли это клетка
    odna_kletka = False
    if x1 == x2:
        if y1 == y2:
            odna_kletka = True

    if odna_kletka:
        print("NO")
    else:
        # считаем разницу по столбцам
        raznica_x = x1 - x2
        if raznica_x < 0:
            raznica_x = raznica_x * (-1)

        # считаем разницу по строкам
        raznica_y = y1 - y2
        if raznica_y < 0:
            raznica_y = raznica_y * (-1)

        # если разницы одинаковые 
        if raznica_x == raznica_y:
            print("YES")
        else:
            print("NO")
