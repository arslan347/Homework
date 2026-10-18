spisok = input('Введите слово:').lower()
formatedspisok = list(spisok)
naoborot = formatedspisok[::-1]

if formatedspisok == naoborot:
    print('Это палиндром')
else:
    print('Это не палиндром')
