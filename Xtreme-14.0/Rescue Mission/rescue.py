import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n = get_number()
    s = [0] + get_numbers()

    from collections import OrderedDict
    from bisect import bisect_left
    mp = OrderedDict()
    mp[0] = 0
    for i in range(1, n + 1):
        mp[i] = s[i]
    mp[n + 1] = 0
    
    d = get_number()
    rescued = 0
    for _ in range(d):
        l, r, v = get_numbers()
        keys = list(mp.keys())

        l_idx = bisect_left(keys, l)
        # print(l_idx, keys, l)
        if keys[l_idx] > l:
            l_idx -= 1
        start = keys[l_idx]
        idx = l_idx + 1
        while keys[idx] <= r:
            mp[start] += s[keys[idx]]
            mp.pop(keys[idx])
            idx += 1
        
        rescued += (r := min(mp[start], v))
        mp[start] -= r
    
    print(rescued)
        
    


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
