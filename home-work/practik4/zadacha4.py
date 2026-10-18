children = int(input("Сколько школьников? "))
mandarini = int(input("Сколько мандаринов? "))
for_one_person = mandarini // children
korzina = mandarini % children
print("Каждому:", for_one_person)
print("Остаток:", korzina)
