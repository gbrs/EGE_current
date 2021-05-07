'''
Задание 5 № 27264
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число следующим образом.
1. Строится двоичная запись числа N.
2. Складываются все цифры полученной двоичной записи. В конец записи (справа) дописывается остаток от деления суммы на 2.
3. Предыдущий пункт повторяется для записи с добавленной цифрой.
4. Результат переводится в десятичную систему и выводится на экран.
Какое наибольшее число, меньшее 100, может появиться на экране в результате работы автомата?
'''

for number in range(100):
    s = bin(number)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    print(int(s, 2))