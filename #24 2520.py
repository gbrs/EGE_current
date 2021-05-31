with open('#24 2520.txt', encoding='utf-8') as f:
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
