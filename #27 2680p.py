with open('#27 2680p.txt') as f:
    cepochka = []
    n = int(f.readline())
    for _ in range(n):
        cepochka.append(list(map(int, f.readline().split())))

cnt_max = 0
cnt = 1
last = cepochka[0][1]
for dominoshka in cepochka[1:]:
    if dominoshka[0] == last:
        last = dominoshka[1]
    elif dominoshka[1] == last:
        last = dominoshka[0]
    else:
        cnt_max = max(cnt, cnt_max)
        cnt = 1
        last = dominoshka[0]  # TODO как переворачивать первую доминошку?
    cnt += 1

