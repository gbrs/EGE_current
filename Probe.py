lst = []
with open('#27 2982p.txt') as f:
    f.readline()
    for number in f:
        lst.append(int(f.readline()))

sm1 = sum(lst)
mx_sum = 0
for i in range(len(lst)):
    sm2 = sm1
    for j in range(len(lst) - 1, 0):
        if sm2 % 71 == 0:
            if mx_sum > sm2:
                mx_sum = sm2
                l = j - i + 1
            elif mx_sum == sum:
                l = j - i + 1
        else:
