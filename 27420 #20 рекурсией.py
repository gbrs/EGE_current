'''
Задание 23 № 27420
Исполнитель преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
Сколько существует программ, для которых при исходном числе 1 результатом является число 20 и при этом
траектория вычислений содержит число 10?
'''


def F(x, y):
    # фактически считает путь от y до x? Всё равно в какую сторону двигаться
    # Так удобнее, чтобы не возиться с проверкой кратности числа (двум в данном примере)
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x * 2, y)


print(F(1, 10) * F(10, 20))
