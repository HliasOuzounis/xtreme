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
    nums = get_numbers()
    
    nums.sort()
    
    left_stack = []
    right_stack = []
    
    for i in nums:
        if not i:
            left_stack.append(i)
            continue
        if not left_stack or left_stack[-1] == 0:
            left_stack.append(i)
        elif not right_stack:
            right_stack.append(i)
        else:
            if left_stack[-1] < right_stack[-1]:
                left_stack.append(i)
            elif left_stack[-1] > right_stack[-1]:
                right_stack.append(i)
            else:
                left_stack.append(i)
    
    left_stack.extend(right_stack[::-1])
    print(sum(left_stack[i] * left_stack[i + 1] for i in range(len(left_stack) - 1)))
    print(*left_stack)


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
