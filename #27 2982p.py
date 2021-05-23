'''
Дана последовательность натуральных трехзначных чисел.
Из неё выбрали некоторые (или все) числа и записали их подряд без пробелов в произвольном порядке.
Определите наибольшее значение с симметричной записью (которая читается одинаково справа налево и слева направо),
которое может быть получено таким образом. Гарантируется, что искомое значение получить можно.
Программа должна вывести сумму цифр найденного значения.
'''

with open('#27 2982p.txt') as f:
    lst = []
    n = int(f.readline())
    for i in range(n):
        lst.append(int(f.readline().strip()))


sm = 0

# если число больше перевернутого, то
# смотрим каких чисел "прямых" или "перевернутых" меньше и
# добавляем к sm удвоенную сумму цифр, исходя из меньшего количества.
# А в случае "симметричного" числа добавляем его цифры максимальное четное число раз (используя // 2)
for number in range(999, 99, -1):
    if number > int(str(number)[::-1]):
        sm += 2 * ((number % 10 + number // 10 % 10 + number // 100) *
              min(lst.count(number), lst.count(int(str(number)[::-1]))))
    elif number == int(str(number)[::-1]):
        sm += 2 * (number % 10 + number // 10 % 10 + number // 100) * (lst.count(number) // 2)

# находим максимальное симметричное число,
# которое встречалось нечетное число раз
# (встречавшиеся четное число раз числа мы уже использовали),
# и добавляем его цифры к нашей сумме
for number in range(999, 99, -1):
    if number == int(str(number)[::-1]):
        print(number, lst.count(number))
        if lst.count(number) % 2 != 0:
            sm += (number % 10 + number // 10 % 10 + number // 100)
            break

print(sm)
