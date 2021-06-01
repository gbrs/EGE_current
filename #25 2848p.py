'''
Рассматриваются целые числа, принадлежащих числовому отрезку [278932; 325396],
которые представляют собой произведение трёх РАЗЛИЧНЫХ простых делителей,
оканчивающихся на одну и ту же цифру.
В ответе запишите количество таких чисел и максимальное из них.
'''


cnt = 0

for number in range(278932, 325396 + 1):

    number_copy = number
    divisor_list = []

    # Перебираем все делители от 2 до корня числа,
    # считая количество делителей.
    for divisor in range(2, int(number**0.5) + 1):
        if number_copy % divisor == 0:
            divisor_list.append(divisor)
            number_copy //= divisor
        # если делится еще раз на тот же делитель, то нас не устраивает такое число
        if number_copy % divisor == 0:
            break
        if len(divisor_list) > 3:
            break
    else:
        # учитываем возможный делитель числа больший корня этого числа
        if number_copy > 1:
            divisor_list.append(number_copy)
        if len(divisor_list) == 3 and divisor_list[0] % 10 == divisor_list[1] % 10 == divisor_list[2] % 10:
            cnt += 1
            mx_number = number
            # если программа долго работает, то лучше принты делать,
            # дабы убедиться, что не завис код
            print(cnt, number, divisor_list)

print(cnt, mx_number)
