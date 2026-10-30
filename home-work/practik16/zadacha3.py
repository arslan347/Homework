a_str = 'data.db image.png log.txt'
b_str = 'image.png script.py data.db'

A = set(a_str.split())
B = set(b_str.split())

common = A.intersection(B)
lost = A.difference(B)

print(' '.join(sorted(common)))
print(' '.join(sorted(lost)))
