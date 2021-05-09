with open('#24 36037.txt') as f:
    s = f.read().strip()

#  в строке XZZYAAAXZZY - отрезок длиной 9!
cnt = 3
mx = 0
for i in range(3, len(s)):
    if not (s[i - 3] == 'X' and s[i - 2] == 'Z' and s[i - 1] == 'Z' and s[i] == 'Y'):
        cnt += 1
        mx = max(mx, cnt)  # каждый раз максимум проверяем поэтому не надо в конце файла отдельно проверять
    else:
        cnt = 3

print(mx)
