#Задание 6
name = input('Ваше имя: ')
age = input('Ваш возраст: ')
subjects = input('Любимые предметы: ')

age = int(age)
subjects_list = subjects.split(',')

student = {
    'name': name,
    'age': age,
    'subjects': subjects_list
}

print('АНКЕТА СТУДЕНТА')
print('Имя:', student['name'])
print('Возраст:', student['age'])
print('Любимые предметы:', student['subjects'])
