import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

MOD = 1000000007
PHI = 500000002

def mod_inverse(a):
    return pow(a, PHI - 1, MOD - 1)

def ncr(n, r):
    r = min(r, n - r)
    
    num = 1
    denom = 1
    for i in range(r):
        num = (num * (n - i)) % (MOD - 1)
        denom = (denom * (i + 1)) % (MOD - 1)
    
    return (num * mod_inverse(denom)) % (MOD - 1)


def solve_case():
    a, b, c = get_numbers()

    power = ncr(b, c)
    print(pow(a, power, MOD))


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
