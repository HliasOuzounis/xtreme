import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


MOD = 10 ** 9 + 7
def populate_dp():
    B = 10 ** 6
    dp = [0] * (B + 1)
    dp[0] = 1
    
    for i in range(1, B + 1):
        dp[i] = 0
        j = 2
        while j - 1 <= i:
            dp[i] = (dp[i] + dp[i - (j - 1)]) % MOD
            j *= 2

    return dp

def populate_idx_sums(dp):
    B = 10 ** 6
    idx_sums = [1] * (B + 1)
    for i in range(1, B + 1):
        idx_sums[i] = (idx_sums[i - 1] + dp[i] * 2) % MOD

    return idx_sums
        
def solve_case(idx_sums):
    a, b = get_numbers()
    start = idx_sums[a - 1] if a != 0 else 0
    end = idx_sums[b]
    return (end - start) % MOD

def main():
    dp = populate_dp()
    idx_sums = populate_idx_sums(dp)
    for test_case in range(total_cases := get_number()):
        print(solve_case(idx_sums))


if __name__ == "__main__":
    main()
