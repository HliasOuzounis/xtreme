import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def solve_case(a, b):
    d = get_number()
    
    result = 0
    for div in range(1, 10**6):
        if div > b:
            break
        
        first = a // div * div
        if first < a:
            first += div
        while first <= b:
            if div % d:
                result += 1
            if ((first / div) % d) and div * div != first and first / div > 10**6:
                result += 1
            first += div
    
    print(result)


def main():
    total_cases, a, b = get_numbers()
    for test_case in range(total_cases):
        solve_case(a, b)


if __name__ == "__main__":
    main()
