'''
Имеется набор данных, состоящий из положительных целых чисел, не превышающих 10000.
Необходимо найти количество троек, в которых сумма первых двух элементов равна третьему элементу.
Порядок элементов тройки должен соответствовать порядку в последовательности.
'''

'''НЕ РЕШИЛ ВТОРОЙ ФАЙЛ: O(n^3)'''

with open('#27 2712p.txt') as f:
    lst = []
    n = int(f.readline())
    for i in range(n):
        lst.append(int(f.readline().strip()))

# print(lst)

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        cnt += lst[j + 1::].count(lst[i] + lst[j])
        if j % 1000 == 0:
            print(i, j)
'''for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if lst[i] + lst[j] == lst[k]:
                # print(i, lst[i], j, lst[j], k, lst[k])
                cnt += 1
        print(i, j)'''

print(cnt)
