'''
Текстовый файл 24-j8.txt состоит не более чем из 106 десятичных цифр.
Найдите максимальную длину последовательности,
каждые две соседние цифры в которой в сумме дают значение не меньшее 10.
В качестве ответа укажите максимальную длину найденной последовательности.
'''

with open('#24 2716p.txt', encoding='utf-8') as f:
    s = list(map(int, f.read()))

cnt = 1
cnt_max = 0

for i in range(1, len(s)):
    if s[i] + s[i - 1] >= 10:
        cnt += 1
    else:
        cnt_max = max(cnt_max, cnt)
        cnt = 1

cnt_max = max(cnt_max, cnt)
print(cnt_max)
