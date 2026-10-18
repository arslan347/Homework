# Ввод значений
ves, rost = map(float, input("Введите ваш вес и рост через пробел: ").split())
# Подсчет ИМТ
IMT = ves / (rost * rost)
# Вывод полученных данных
print(f"Ваш ИМТ: {IMT:,.1f}")
