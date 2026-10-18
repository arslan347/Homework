# Ввод значений
weight, height = map(float, input("Введите ваш вес и рост через пробел: ").split())
# Подсчет ИМТ
IMT = weight / (height * height)
# Вывод полученных данных
print(f"Ваш ИМТ: {IMT:,.1f}")
