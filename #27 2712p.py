'''
Имеется набор данных, состоящий из положительных целых чисел, не превышающих 10000.
Необходимо найти количество троек, в которых сумма первых двух элементов равна третьему элементу.
Порядок элементов тройки должен соответствовать порядку в последовательности.
'''

with open('#27 2982p.txt') as f:
    lst = []
    n = int(f.readline())
    for i in range(n):
        lst.append(int(f.readline().strip()))

st = set(lst)
# print(lst)

cnt = 0
for i in range(60000 - 1):
    for j in range(i + 1, 60000):
        if lst[i] + lst[j] in st:
            cnt += 1
    if i % 100 == 0:
        print(i)

print(cnt)
