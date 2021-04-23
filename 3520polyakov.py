for i in range(100):
    s = bin(i)[2:]
    for _ in range(2):
        if s.count('1') > s.count('0'):
            s = s + '0'
        else:
            s = '11' + s
    R = int(int(s, 2))
    if R > 500:
        print(i, R)
        break

