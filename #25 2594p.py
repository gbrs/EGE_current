'''
Среди целых чисел, принадлежащих числовому отрезку [2031; 14312],
найдите числа, которые не содержат цифру 2,
если записать их в системе счисления с основанием 11.
Ответом будет максимум среди найденных чисел.
'''

'''непродуманная задача: надо идти от больших чисел и найдя его закончить?'''


for number in range(14312, 2031 - 1, -1):
    copy_number = number
    # разбираем число на цифры
    while copy_number > 0:
        # если встретили двойку, то число нас не интересует
        if copy_number % 11 == 2:
            break
        else:
            copy_number //= 11
    else:
        print(number)
        break

