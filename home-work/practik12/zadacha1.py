m = input('Введите число больше единицы')
m = int(m)
spisok = []
for i in range(1, m + 1):
    if i % 2 == 1:
        spisok.append(i)
print(spisok)
