for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # (x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w
                if (x or y) and not(y == z) and not w == 1:
                    print(z, y, x, w)

# следование заменяют на <=
