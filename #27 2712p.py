'''
Имеется набор данных, состоящий из положительных целых чисел, не превышающих 10000.
Необходимо найти количество троек, в которых сумма первых двух элементов равна третьему элементу.
Порядок элементов тройки должен соответствовать порядку в последовательности.
'''

with open('#27 2712p_small.txt') as f:
    lst = []
    n = int(f.readline())
    for i in range(n):
        lst.append(int(f.readline().strip()))

st = set(lst)
print(lst)

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(i + 2, n):
            if lst[i] + lst[j] == lst[k]:
                print(lst[i], lst[j], lst[k])
                cnt += 1

print(cnt)
