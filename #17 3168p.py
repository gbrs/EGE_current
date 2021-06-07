'''
Назовём натуральное число подходящим,
если ровно два из его делителей входят в список (7, 13, 17, 19).
Найдите все подходящие числа, принадлежащих отрезку [25000; 35000]
В ответе запишите два целых числа: сначала количество,
затем сумму цифр всех найденных чисел.
'''


cnt = sm = 0

for number in range(25000, 35000 + 1):
    cnt_divisors = 0
    for divisor in 7, 13, 17, 19:
        if number % divisor == 0:
            cnt_divisors += 1
    if cnt_divisors == 2:
        sm += (number // 10000 +
               number // 1000 % 10 +
               number // 100 % 10 +
               number // 10 % 10 +
               number % 10)
        cnt += 1

print(cnt, sm)
