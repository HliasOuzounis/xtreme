import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def solve_case():
    from math import log2, ceil
    n, m, s = get_numbers()
    print(ceil(log2(n - 1)) * s + m * (n - 1))


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
