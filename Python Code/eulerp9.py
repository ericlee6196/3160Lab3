
product,csquared = 0,0

for a in range(3, 1000):
    for b in range (a + 1, 999):
        csquared = a**2 + b**2
        c = csquared**0.5

        if a + b + c == 1000:
            product = a * b * c
print(product)