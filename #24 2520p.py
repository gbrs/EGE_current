'''
В текстовом файле k7a-6.txt находится цепочка из
символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, не содержащей гласных букв.
'''

with open('#24 2520p.txt', encoding='utf-8') as f:
    s = f.read()

cnt = 0
cnt_max = 0

for char in s:
    if char in 'BCDF':
        cnt += 1
    else:
        cnt_max = max(cnt_max, cnt)
        cnt = 0

cnt_max = max(cnt_max, cnt)
print(cnt_max)
