import sys
from math import ceil


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def get_limit(a, b):
    return ceil((a - 1) / (b - a))


def solve_case():
    n, a, b = get_numbers()
    if a == b:
        if n % a == 0:
            print("YES")
            print(*[a] * (n // a))
        else:
            print("NO")
        return
    
    k = get_limit(a, b) + 1

    seq = []
    
    while n > k * b:
        n -= b
        seq.append(b)
    
    # while n < k * a:
    #     k -= 1
    k = min(k, n // a)
    
    if n > k * b:
        print("NO")
        return
    
    n -= k * a
    
    while n != 0:
        if a + n > b:
            seq.append(b)
            k -= 1
            n -= b - a
        else:
            seq.append(a + n)
            k -= 1
            n = 0
            
    seq += [a] * k
    
    print("YES")
    print(*seq[::-1])

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
