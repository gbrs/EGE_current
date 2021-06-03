'''
Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678],
которые представляют собой произведение трёх различных простых делителей,
оканчивающихся на одну и ту же цифру.
В ответе запишите количество таких чисел и такое из них,
для которого разность наибольшего и наименьшего простых делителей минимальна.
'''


cnt = 0
difference = 1000000

for number in range(485617, 529678 + 1):

    number_copy = number
    divisor_lst = []
    flag = True

    # Перебираем все делители от 2 до корня числа.
    for divisor in range(2, int(number**0.5) + 1):

        if number_copy % divisor == 0:
            divisor_lst.append(divisor)
            number_copy //= divisor
            # делим на делитель пока делится
            if number_copy % divisor == 0 or len(divisor_lst) > 3:
                flag = False
                break

        # проверяем не разложили ли число полностью
        if number_copy <= 1:
            break

    # учитываем возможный делитель числа больший корня этого числа,
    # но не само это число (на случай, если число простое)
    else:
        divisor_lst.append(number_copy)

    # распечатываем подходящие варианты
    if len(divisor_lst) == 3 and divisor_lst[0] % 10 == divisor_lst[1] % 10 == divisor_lst[2] % 10 and flag is True:
        cnt += 1
        # принт позволяющий вывести наши ответы, чтобы перепроверить в экселе
        print(number, *divisor_lst)
        if divisor_lst[2] - divisor_lst[0] < difference:
            difference = divisor_lst[2] - divisor_lst[0]
            my_number = number

print(cnt, my_number)
