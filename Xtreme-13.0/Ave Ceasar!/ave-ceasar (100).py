import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def check_string(nums):
    if len(nums) == 1:
        return True
    
    diffs = [0] * len(nums)
    for i, c in enumerate(nums[:-1], start=1):
        diffs[i] = nums[i] - nums[i - 1]
    
    if all(diff >= 0 for diff in diffs):
        return True
    
    valid = False
    for i, diff in enumerate(diffs):
        if diff < 0:
            valid = check_string(nums[:i]) and check_string(nums[i:]) and smaller(nums[:i], nums[i:])
            
        if valid:
            return True
        
    return False

def smaller(a, b):
    for ai, bi in zip(a, b):
        if ai > bi:
            return False
        if ai < bi:
            return True
    
    return len(a) <= len(b)


def solve_case():
    string = get_word()
    to_numbers = tuple(ord(char) - ord('A') for char in string)
    
    print('1' if check_string(to_numbers) else '0', end='')

def main():
    for test_case in range(total_cases := get_number()):
        solve_case()
    print()


if __name__ == "__main__":
    main()
