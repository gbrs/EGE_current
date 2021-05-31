'''
Текстовый файл 24-1.txt состоит не более чем из 106 символов -
заглавных латинских букв и цифр. Определите максимальное число,
состоящее только из чётных цифр.
'''

with open('#24 2528p.txt', encoding='utf-8') as f:
    s = f.read()

# все числа записываем в список
number = ''
lst = []
for char in s:
    if char in '0123456789':
        number += char
    elif len(number) > 0:
        lst.append(number)
        number = ''

# бежим по списку и ищем числа, состоящие только из четных цифр.
# Если чило такое, то проверяем его на максимальность.
mx = -1
for number in lst:
    for char in number:
        if char in '13579':
            break
    else:
        mx = max(mx, int(number))

print(mx)
