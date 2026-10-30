c_str = 'Bond Smith Hunt'
m_str = 'Bond Power Hunt'
k_str = 'Petrov Hunt Ivanov'

C = set(c_str.split())
M = set(m_str.split())
K = set(k_str.split())

# Находим общих для ЦРУ и МИ-6, и убираем тех, кто есть в КГБ
double_agents = C.intersection(M).difference(K)

print(' '.join(sorted(double_agents, reverse=True)))
