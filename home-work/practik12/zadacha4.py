marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
ammount5 = 0
ammount2 = 0
for i in marks:
    if i % 5 == 0:
        ammount5 += 1
    elif i % 2 == 0 and i != 4:
        ammount2 += 1
print('Колличество пятерок:', ammount5, 'Колличество двоек:', ammount2)
