'''
Задание 19 № 27416
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может добавить в одну из куч (по своему выбору) один камень или увеличить
количество камней в куче в два раза. Например, пусть в одной куче 10 камней, а в другой 5 камней; такую позицию в игре
будем обозначать (10,5). Тогда за один ход можно получить любую из четырёх позиций: (11,5), (20,5), (10,6), (10,10).
Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.

Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 77.
Победителем считается игрок, сделавший последний ход, т. е. первым получивший такую позицию,
при которой в кучах будет 77 или больше камней.

В начальный момент в первой куче было семь камней, во второй куче — S камней; 1 ≤ S ≤ 69.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Описать стратегию игрока — значит описать, какой ход он должен сделать в любой ситуации, которая ему может встретиться
при различной игре противника. В описание выигрышной стратегии не следует включать ходы играющего по этой стратегии
игрока, не являющиеся для него безусловно выигрышными, т. е. не являющиеся выигрышными независимо от игры противника.

Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S,
когда такая ситуация возможна.

+1 *2   >76  1к-7
'''


field = [[''] * 100 for _ in range(100)]
# print(field)

for i in range(100):
    for j in range(100):
        if i + j > 76:
            field[i][j] = 0

for i in range(100):
    for j in range(100):
        if field[i][j] == '' and (2 * i + j > 76 or i + 2 * j > 76):
            field[i][j] = 1

for i in range(100):
    for j in range(100):
        print(field[i][j], end=' ')
    print()

