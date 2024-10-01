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
    B = 10 ** 5
    dp = [0] * (B + 1)
    dp[0] = 1
    
    for i in range(1, B + 1):
        dp[i] = 0
        j = 2
        while j - 1 <= i:
            dp[i] = (dp[i] + dp[i - (j - 1)]) % MOD
            j *= 2

    return dp
        
        
def solve_case(dp):
    b = get_number()
    if b == 0:
        return 1
    return dp[b] * 2 % MOD

def main():
    dp = populate_dp()
    for test_case in range(total_cases := get_number()):
        print(solve_case(dp))


if __name__ == "__main__":
    main()
