def squareRoot(n):
    x = n
    while abs(x*x - n) > 0.000001:
        x = (x + n / x) / 2
    return x
print(squareRoot(5))
