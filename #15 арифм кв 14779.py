'''
Задание 15 № 14779
Сколько существует целых значений числа A, при которых формула
((x < 5) → (x2 < A)) /\ ((y2 ≤ A) → (y ≤ 5))
тождественно истинна при любых целых неотрицательных x и y?
'''


for A in range(0, 100):
    for x in range(0, 100):
        flag = False
        for y in range(0, 100):
            if (((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5))) is False:
                flag = True
                break
        if flag is True:
            break
    else:
        print(A)

# ВЕЗДЕ ставить скобки в выражениях!!!
