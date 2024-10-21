import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def manacher(s):
    ss = '#' + '#'.join(s) + '#'

    RL = [0] * len(ss)
    max_right, mr_center = -1, -1

    for i in range(len(ss)):
        R = 1
        if i < max_right:
            mr_mirror = mr_center - (i - mr_center)
            R = min(RL[mr_mirror], max_right - i)

        while i - R >= 0 and i + R < len(ss) and ss[i - R] == ss[i + R]:
                R += 1

        RL[i] = R
        if max_right < i + R-1:
            max_right = i + R-1
            mr_center = i

    return RL

def solve_case():
    s = get_word()
    
    m = manacher(s)
    
    even = m[2:-2:2]
    odd = m[1::2]
    
    odd_n = len(odd)
    even_n = len(even) + 2
    
    starts_at_odd = [0] * odd_n
    ends_at_odd = [0] * odd_n
    
    starts_at_even = [0] * even_n
    ends_at_even = [0] * even_n
    
    for i, v in enumerate(odd):
        start = i - (v - 1) // 2
        end = i + (v - 1) // 2
        
        starts_at_odd[start] = max(starts_at_odd[start], v - 1)
        ends_at_odd[end] = max(ends_at_odd[end], v - 1)
    
    for i, v in enumerate(even):
        start = i - (v - 1) // 2 + 1
        end = i + (v - 1) // 2 + 1
        
        starts_at_even[start] = max(starts_at_even[start], v - 1)
        ends_at_even[end] = max(ends_at_even[end], v - 1)
    
    
    for i in reversed(range(1, even_n - 1)):
        ends_at_even[i] = max(ends_at_even[i], ends_at_even[i + 1] - 2)
    
    for i in range(1, even_n - 1):
        starts_at_even[i] = max(starts_at_even[i], starts_at_even[i - 1] - 2)
    
    for i in range(1, odd_n - 1):
        starts_at_odd[i] = max(starts_at_odd[i], starts_at_odd[i - 1] - 2)
    
    for i in reversed(range(1, odd_n - 1)):
        ends_at_odd[i] = max(ends_at_odd[i], ends_at_odd[i + 1] - 2)
    
    for i in reversed(range(even_n - 1)):
        starts_at_even[i] = max(starts_at_even[i], starts_at_even[i + 1])
    for i in range(1, even_n):
        ends_at_even[i] = max(ends_at_even[i], ends_at_even[i - 1])
    
    for i in reversed(range(odd_n - 1)):
        starts_at_odd[i] = max(starts_at_odd[i], starts_at_odd[i + 1])
    for i in range(1, odd_n):
        ends_at_odd[i] = max(ends_at_odd[i], ends_at_odd[i - 1])
    
    ans = 0
    for i in range(1, odd_n):
        temp = starts_at_odd[i] + max(ends_at_even[i], ends_at_odd[i - 1])
        ans = max(ans, temp)
    
    for i in range(1, even_n - 1):
        temp = starts_at_even[i] + max(ends_at_even[i - 1], ends_at_odd[i - 1])
        ans = max(ans, temp)
    
    print(ans)
    
    
def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
