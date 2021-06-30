from math import log10

# karatsuba multiplication
# implemented from Tim Roughgarden's Algorithms course
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(int(log10(x)), int(log10(y))) + 1       #  max number of digits
        n_over_2 = n // 2

        # split x in two halves
        a = x // 10**n_over_2
        b = x % 10**n_over_2

        # split y in two halves
        c = y // 10**n_over_2
        d = y % 10**n_over_2

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd

        return (ac * 10**(2*n_over_2)) + (ad_plus_bc * 10**n_over_2) + bd