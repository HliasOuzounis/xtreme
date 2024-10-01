import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    k, j = get_numbers()
    if k < j:
        k, j = j, k
    
    total = 0
    diff = k - j
    if diff > j:
        total += j
        k -= j * 2
        j = 0
    else:
        total += diff
        k = j - diff
        j = k
    
    if j != 0:
        total += (k + j) // 3
        
    print(total)

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
