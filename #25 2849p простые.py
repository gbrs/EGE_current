'''
Рассматриваются целые числа, принадлежащих числовому отрезку [158928; 345293],
которые представляют собой произведение трёх РАЗЛИЧНЫХ простых делителей.
В ответе запишите количество таких чисел и минимальное из них.
'''


cnt = 0

for number in range(345293, 158928 - 1, -1):

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
        if len(divisor_list) == 3:
            cnt += 1
            mn_number = number
            # если программа долго считает, то неплохо бы принты какие-то включить,
            # чтобы убедиться, что она не зависла
            print(cnt, number, divisor_list)

print(cnt, mn_number)
