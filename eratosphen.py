size = int(input())
lst = []
for i in range(size + 1):
    lst.append(i)
lst[0] = lst[1] = 0
print(lst)

for i in range(size + 1):
    if lst[i] > 0:
        j = 2 * i
        while j <= size:
            lst[j] = 0
            j += i
        print(lst)

print(lst)
