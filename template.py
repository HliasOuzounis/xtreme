import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


# numpy and scipy are available for use
import numpy
import scipy


def solve_case():
    pass


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
