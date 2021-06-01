'''
Рассматриваются целые числа, принадлежащих числовому отрезку [278932; 325396],
которые представляют собой произведение трёх РАЗЛИЧНЫХ(?) простых делителей,
оканчивающихся на одну и ту же цифру.
В ответе запишите количество таких чисел и максимальное из них.
'''

'''НЕ ПОЛУЧИЛОСЬ!!! максимальное число верное, а вот количество чисел - нет.
НЕПРАВИЛЬНО!!! слишком долго'''

cnt = 0

for number in range(278932, 325396 + 1):

    number_copy = number
    divisor_list = []

    # Перебираем все делители от 2 до корня числа,
    # считая количество делителей.
    # Вообще-то эффективнее через while,
    # а я всегда бегу до корня, хотя уже число и "закончилось".
    # Но так код понятнее.
    for divisor in range(2, int(number**0.5) + 1):
        if number_copy % divisor == 0:
            divisor_list.append(divisor)
        # делим число на делитель пока оно на него делится
        while number_copy % divisor == 0:
            number_copy //= divisor
        if len(divisor_list) > 3:
            break
    else:
        if len(divisor_list) == 3 and divisor_list[0] % 10 == divisor_list[1] % 10 == divisor_list[2] % 10:
            cnt += 1
            mx_number = number
            print(cnt, number, divisor_list)

print(cnt, mx_number)
