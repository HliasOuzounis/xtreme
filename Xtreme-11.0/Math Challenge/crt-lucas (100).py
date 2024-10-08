import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

MOD = 1000000007
p1 = 2
p2 = 500000003
assert (p1 * p2 + 1) == MOD

def mod_inverse(a, mod):
    return pow(a, mod - 2, mod)

def ncr(n, r, mod):
    r = min(r, n - r)
    
    num = 1
    denom = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        denom = (denom * (i + 1)) % mod
        
    denom = mod_inverse(denom, mod)
    
    return (num * denom) % mod

def ncr_parity(n, r):
    return (r & (n - r)) == 0
    

def solve_case():
    a, b, c = get_numbers()
    
    a1 = ncr_parity(b, c)
    a2 = ncr(b, c, p2)

    power = (a1 * mod_inverse(p2, p1) * p2 + a2 * mod_inverse(p1, p2) * p1) % (p1 * p2)
    
    print(pow(a, power, MOD))


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
