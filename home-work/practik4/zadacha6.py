import math

x = float(input("Введите значение (в градусах): "))
radian = math.radians(x)
result = math.sin(radian) + math.cos(radian) + math.tan(radian)**2
print("Ответ:", result)
