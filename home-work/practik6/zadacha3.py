# получаем данные
stroka = input()
chisla = stroka.split()

# преобразуем в числа
a = int(chisla[0])  # столбец 1
b = int(chisla[1])  # строка 1
c = int(chisla[2])  # столбец 2
d = int(chisla[3])  # строка 2

# если всё хорошо
vse_ok = True

# проверяем первое число
if a < 1:
    vse_ok = False
if a > 8:
    vse_ok = False

# проверяем второе число
if b < 1:
    vse_ok = False
if b > 8:
    vse_ok = False

# проверяем третье число
if c < 1:
    vse_ok = False
if c > 8:
    vse_ok = False

# проверяем четвёртое число
if d < 1:
    vse_ok = False
if d > 8:
    vse_ok = False

if vse_ok == False:
    print("ошибка ввода")
else:
    # считаем цвет первой клетки
    summa1 = a + b
    ostatok1 = summa1 % 2
    
    # считаем цвет второй клетки
    summa2 = c + d
    ostatok2 = summa2 % 2
    
    # сравниваем цвета
    if ostatok1 == ostatok2:
        print("YES")
    else:
        print("NO")
