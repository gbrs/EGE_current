'''
Дана последовательность N целых неотрицательных чисел.
Необходимо определить количество пар положительных элементов этой последовательности,
сумма которых четна, при этом между элементами пары есть хотя бы один ноль.
'''

with open('#27 2710p.txt') as f:
    lst = []
    n = int(f.readline())
    for _ in range(n):
        lst.append(int(f.readline()))


cnt = odd = even = current_odd = current_even = 0

for number in lst:
    if number == 0:
        even += current_even
        odd += current_odd
        current_odd = current_even = 0
    elif number % 2 == 0:
        cnt += even
        current_even += 1
    else:
        cnt += odd
        current_odd += 1

print(cnt)
