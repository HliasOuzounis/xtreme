import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


from math import log2

def xor_range(l, r):
    nof_bits = int(log2(r)) + 1

    ans = 0
    for bit in range(nof_bits):
        l_bit = get_xor_for_bit(bit, l - 1)
        r_bit = get_xor_for_bit(bit, r)
        ans |= r_bit ^ l_bit
        
    return ans
    
def get_xor_for_bit(bit, x):
    if bit == 0:
        return 1 if (x & 2) >> 1 != x % 2 else 0
    div = 1 << bit
    mod = x % (div * 2)
    if mod < div:
        return 0
    return 0 if mod % 2 else div
    
def solve_case():
    l, h, n, d1, d2 = get_numbers()
    
    ans = xor_range(n, n + l * h - 1)
    
    row1, col1 = divmod(d1 - n, l)
    row2, col2 = divmod(d2 - n, l)
    if row1 > row2:
        row1, row2 = row2, row1
    if col1 > col2:
        col1, col2 = col2, col1
    
    for row in range(row1, row2 + 1):
        L = n + row * l + col1
        R = n + row * l + col2
        ans ^= xor_range(L, R)
        print(xor_range(L, R))
        
    print(ans)

def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
