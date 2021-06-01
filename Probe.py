for divisor in range(2, int(number ** 0.5) + 1):
    if number_copy % divisor == 0:
        divisor_list.append(divisor)
        number_copy //= divisor
    if number_copy % divisor == 0:
        break
    if len(divisor_list) > 3:
        break