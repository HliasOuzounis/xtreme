import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def kadane(arr, find_max=True):
    n = len(arr)
    ans = 0
    s = 0
    for i in range(n):
        s += arr[i]
        ans = max(ans, s) if find_max else min(ans, s)
        s = max(s, 0) if find_max else min(s, 0)
    return ans


def solve_case():
    n, m = get_numbers()
    a = get_numbers()
    b = get_numbers()
    
    max_ans = kadane(a, find_max=True)  * kadane(b, find_max=True)
    min_ans = kadane(a, find_max=False) * kadane(b, find_max=False)
    
    # all ai > 0 and all bi < 0
    # kadane(a, find_max=False) == 0 and kadane(b, find_max=True) == 0
    if max_ans == 0 and min_ans == 0:
        min_ans = min(a) * max(b)
        max_ans = max(a) * min(b)
        
    print(max(max_ans, min_ans))
    
    
def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
