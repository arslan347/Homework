log1_str = input('Введите IP для первого лога: ')
log2_str = input('Введите IP для второго лога: ')
log3_str = input('Введите IP для третьего лога: ')

log1 = set(log1_str.split())
log2 = set(log2_str.split())
log3 = set(log3_str.split())

all_ips = log1.union(log2).union(log3)
everywhere = log1.intersection(log2).intersection(log3)

suspicious = all_ips.difference(everywhere)

print(" ".join(sorted(suspicious)))
