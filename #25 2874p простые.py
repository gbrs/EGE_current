'''
Найдите в диапазоне [2; 20000] числа, каждое из которых
имеет максимальное количество простых делителей среди всех таких чисел.
Выведите минимальное из таких чисел и через пробел количество его простых делителей.
'''

'''
имеется ввиду максимальное количество уникальных делителей: у 1024 их 1
'''


mx_divisors = 0

for number in range(2, 20000 + 1):

    number_copy = number
    divisor_cnt = 0

    # Перебираем все делители от 2 до корня числа.
    for divisor in range(2, int(number**0.5) + 1):
        # считаем только уникальные делители
        if number_copy % divisor == 0:
            divisor_cnt += 1
            # делим на делитель пока делится
            while number_copy % divisor == 0:
                number_copy //= divisor
        # проверяем не разложили ли число полностью
        if number_copy <= 1:
            break
    else:
        # учитываем возможный делитель числа, больший корня этого числа
        if number_copy > 1:
            divisor_cnt += 1

    # строгое равенство позволяет заполнить наименьшее из чисел
    # (нестрогое запомнило бы наибольшее)
    if divisor_cnt > mx_divisors:
        mx_divisors = divisor_cnt
        my_number = number

print(my_number, mx_divisors)
