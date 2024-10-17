import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def kadane(arr):
    n = len(arr)
    ans = arr[0]
    s = 0
    for i in range(n):
        s += arr[i]
        ans = max(ans, s)
        s = max(s, 0)
    return ans


def solve_case():
    n, m = get_numbers()
    a = get_numbers()
    b = get_numbers()

    if n < m:
        n, m = m, n
        a, b = b, a

    ans = float("-inf")
    for l in range(m):
        row_sum = [0] * n
        for r in range(l, m):
            for i in range(n):
                row_sum[i] += a[i] * b[r]

            ans = max(ans, kadane(row_sum))

    print(ans)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
