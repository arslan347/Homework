import math

x1 = float(input("Введите значение для x1: "))
y1 = float(input("Введите значение для y1: "))
x2 = float(input("Введите значение для x2: "))
y2 = float(input("Введите значение для y2: "))
evklidovo_number = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("Ответ:", evklidovo_number)
