print("Задание №1")
my_list = [1, 2, 3]
print(my_list)
my_list[0] = 100
print(my_list)
# У нас есть возможность менять все

print("Задание №2")
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple[0] = 100
# Уже не получается, так как выходит ошибка в связи с тем что кортеж нельзя менять
# Ошибка: TypeError: 'tuple' object does not support item assignment

print("Задание №3")
my_string = "cat"
print(my_string)
my_string[0] = "b"
# У нас нет возможности поменять, то есть невозможно поменять отдельный символ, поэтому выходит ошибка
# Ошибка: TypeError: 'str' object does not support item assignment
