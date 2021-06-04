'''
Рассматривается множество целых чисел,
принадлежащих числовому отрезку [862346; 1056242].
Найдите числа, нетривиальные делители которых
образуют арифметическую прогрессию с разностью d = 100.
В ответе для каждого такого числа (в порядке возрастания)
запишите сначала само число, а потом – его максимальный нетривиальный делитель.
'''

'''что-то не придумать эффективность как повысить. 
Минут 15, наверное, работать будет'''

for number in range(862346, 1056242 + 1):
    if number % 500 == 0:
        print(number)
    old_divisor = 'first'
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            if divisor % 100 != number // divisor % 100:
                break
            if old_divisor == 'first':
                old_divisor = divisor
                if number % (old_divisor + 100) != 0:
                    break
                continue
            elif divisor - old_divisor == 100:
                old_divisor = divisor
            else:
                break
    else:
        if old_divisor != 'first' and old_divisor != number // old_divisor:
            print(number, old_divisor)
