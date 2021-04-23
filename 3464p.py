for i in range(100, 200):
    s = '1' * i
    while '333' in s or '111' in s:
      s = s.replace('333', '11', 1)
      s = s.replace('111', '3', 1)
    print(i, s)
