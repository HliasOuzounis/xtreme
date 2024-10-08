# ---------------- Primes ---------------- #

def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n
    """
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return primes


# ---------------- Modulo ---------------- #
# https://sites.math.washington.edu//~greenber/Congruences.pdf

MOD = 998244353
MOD = 10**9 + 7


def mod_inverse_prime(a):
    """
    Get the modular inverse of a assuming mod is prime
    using Fermat's little theorem
    a**(p-1) = 1 mod p
    """
    # Python's pow method returns base**exp % mod
    return pow(base=a, exp=MOD - 2, mod=MOD)


def nCr_with_mod(n, r):
    """
    Efficiently calculate nCr(n, r) % mod, mod is prime
    """
    r = min(r, n - r)

    numerator = 1
    denominator = 1

    for i in range(r):
        numerator = (numerator * (n - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD

    return (numerator * mod_inverse_prime(denominator)) % MOD

def ncr_parity(n, r):
    """
    True if nCr(n, r) is odd, False if even 
    Consequence of Lucas' Theorem 
    (https://en.wikipedia.org/wiki/Lucas%27s_theorem)
    (https://math.stackexchange.com/a/11009)
    """
    return (r & (n - r)) == 0