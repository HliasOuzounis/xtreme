# ---------------- Integers ---------------- #


def all_common_divisors(n1, n2):
    """
    Generator that returns all common divisors of two numbers in descending order (except 1)
    """
    if n2 % n1 == 0:
        yield n1
    n1, n2 = min(n1, n2), max(n1, n2)
    for i in range(int(n1 // 2) + 1, 1, -1):
        if n1 % i == 0 and n2 % i == 0:
            yield i


def gcd_Euclid(a, b):
    """
    returns the greatest common divisor of two numbers a, b (a < b)
    """
    if b == 0:
        return a
    return gcd_Euclid(b, a % b)


def fast_expontiation(base, exp, mod):
    """
    Fast exponentiation algorithm to calculate base**exp % mod
    equivilant to pow(base, exp, mod) in python
    but can be used for matrices and other types
    """
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def smallest_divisible(n, p):
    """
    Find the smallest number x (x > n) that is divisible by p
    """
    smallest = n // p * p
    if smallest < n:
        smallest += p
    return smallest


def xor_range(x):
    """
    Calculate the xor of all numbers from 0 to x
    """
    match x % 4:
        case 0:
            return x
        case 1:
            return 1
        case 2:
            return x + 1
        case _:
            return 0