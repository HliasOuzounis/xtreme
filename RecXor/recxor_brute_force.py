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
    l, h, n, d1, d2 = get_numbers()
    
    ans = 0
    row1, col1 = divmod(d1 - n, l)
    row2, col2 = divmod(d2 - n, l)
    
    if row1 > row2:
        row1, row2 = row2, row1
    if col1 > col2:
        col1, col2 = col2, col1
    
    for row in range(h):
        for col in range(l):
            if row1 <= row <= row2 and col1 <= col <= col2:
                continue
            num = n + row * l + col
            ans ^= num
    
    print(ans)


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
