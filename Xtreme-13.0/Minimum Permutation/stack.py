import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n, m = get_numbers()
    a = get_numbers()
    s = get_numbers()
    
    stack = sorted(s, reverse=True)
    
    idx = 0
    new_arr = []
    while stack:
        while idx < n and stack[-1] > a[idx]:
            new_arr.append(a[idx])
            idx += 1
        new_arr.append(stack.pop())
        
    while idx < n:
        new_arr.append(a[idx])
        idx += 1
    
    print(*new_arr)
    


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
