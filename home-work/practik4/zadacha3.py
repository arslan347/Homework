number = int(input("Введите четырехзначное число: "))
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
print("Цифра в тысячах:", a)
print("Цифра в сотнях:", b)
print("Цифра в десятках:", c)
print("Цифра в единицах:", d)
