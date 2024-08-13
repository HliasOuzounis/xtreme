import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


# numpy and scipy are available for use
# import numpy
# import scipy


def solve_case():
    l, h, n, d1, d2 = get_numbers()
    
    # table = numpy.zeros((h, l), dtype=numpy.int16)
    table = [[0] * l for _ in range(h)]
    
    for num in range(n, n + l * h):
        row, col = divmod(num - n, l)
        table[row][col] = num
        if row > 0:
            table[row][col] ^= table[row - 1][col]
        if col > 0:
            table[row][col] ^= table[row][col - 1]
        if row > 0 and col > 0:
            table[row][col] ^= table[row - 1][col - 1]
    
    row1, col1 = divmod(d1 - n, l)
    row2, col2 = divmod(d2 - n, l) 
    
    if row1 > row2:
        row1, row2 = row2, row1
    if col1 > col2:
        col1, col2 = col2, col1
    
    ans = table[row2][col2] ^ table[-1][-1]
    if row1 > 0:
        ans ^= table[row1 - 1][col2]
    if col1 > 0:
        ans ^= table[row2][col1 - 1]
    if row1 > 0 and col1 > 0:
        ans ^= table[row1 - 1][col1 - 1]
    
    print(ans)


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
