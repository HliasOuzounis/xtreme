import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

# 0 ^ 1 ^ 2 ^ 3 == 0
# 4 ^ 5 ^ 6 ^ 7 == 0
# ... 4 consecutive numbers (starting with 4k) have xor 0
# if x % 4 == 0:
    # (0 ^ 1 ^ 2 ^ 3 ^ ... x - 1) ^ x == 0 ^ x == x
# if x % 4 == 1:
    # (0 ^ 1 ^ 2 ^ 3 ^ ... x - 2) ^ (x - 1 ^ x) == 0 ^ (x - 1 ^ x) == 1
# if x % 4 == 2:
    # (0 ^ 1 ^ 2 ^ 3 ^ ... x - 3) ^ (x - 2 ^ x - 1 ^ x) == 0 ^ (x - 2 ^ x - 1 ^ x) == (1 ^ x) = x + 1 (x is even)
# if x % 4 == 3:
    # (0 ^ 1 ^ 2 ^ 3 ^ ... x - 4) ^ (x - 3 ^ x - 2 ^ x - 1 ^ x) == 0 ^ (x - 3 ^ x - 2 ^ x - 1 ^ x) == (x ^ x) = 0
                                                                        # (x - 3 ^ x - 2 ^ x - 1) == x - 1 + 1 = x
def xor_range(x):
    match x % 4:
        case 0:
            return x
        case 1:
            return 1
        case 2:
            return x + 1
        case _:
            return 0


def solve_case():
    l, h, n, d1, d2 = get_numbers()

    ans = xor_range(n - 1) ^ xor_range(n + l * h - 1)
    
    row1, col1 = divmod(d1 - n, l)
    row2, col2 = divmod(d2 - n, l)
    if row1 > row2:
        row1, row2 = row2, row1
    if col1 > col2:
        col1, col2 = col2, col1

    for row in range(row1, row2 + 1):
        L = n + row * l + col1
        R = n + row * l + col2
        ans ^= xor_range(L - 1) ^ xor_range(R)

    print(ans)


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
