'''
НЕ РАБОТАЕТ!!!
'''

'''
Задание 15 № 34541
На числовой прямой даны два отрезка: Р = [3, 38] и Q = [21, 57].
Какова наибольшая возможная длина интервала A,
что логическое выражение ((х ∈ Q) → (х ∈ Р)) → ¬(х ∈ A) тождественно истинно, 
то есть принимает значение 1 при любом значении переменной х.
'''


P = range(3, 38 + 1)
Q = range(21, 57 + 1)

A = range()

for x in range(1, 100):
    z = ((x in Q) <= (x in P)) <= (x not in A)
    if z is False:
        print('Неа')
        break
else:
    print(A)
