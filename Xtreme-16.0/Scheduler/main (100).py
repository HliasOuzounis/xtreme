N, M = list(map(int, input().split()))

jobs = list(map(int, input().split()))

MOD = 10**9 + 7

if M == 1:
    ans = sum(pow(2, i, MOD) for i in jobs)
else:
    ans = pow(2, max(jobs), MOD)

print(ans % MOD)
