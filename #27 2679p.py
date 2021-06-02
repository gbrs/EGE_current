'''
Имеется набор данных, состоящий из целых чисел.
Необходимо определить максимальное произведение подпоследовательности,
состоящей из одного или более идущих подряд элементов.
'''

with open('#27 2679p.txt') as f:
    lst = []
    n = int(f.readline())
    for _ in range(n):
        lst.append(int(f.readline()))


p_max = 0
p = 1
mx_min = -101

# Ищем произведение пока не наткнемся на ноль. Тогда сверяем с максимумом.
# На случай с отрицательным произведением,
# запоминаем самый большой (т.е. наименьший по модулю) из отрицательных элементов
# и делим на него произведение.
for number in lst:
    if number != 0:
        p *= number
        if number < 0:
            mx_min = max(number, mx_min)
    elif p > 0:
        p_max = max(p, p_max)
        p = 1
        mx_min = -101
    elif p <= 0:
        p_max = max(p // mx_min, p_max)
        p = 1
        mx_min = -101


p_max = max(p, p_max)

print(p_max)
