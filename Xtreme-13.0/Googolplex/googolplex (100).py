import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def phi(n):
    # Euler's totient function for n = 10 ** Y
    return n - n // 2 - n // 5 + n // 10


def solve_case():
    x, y = get_numbers()
    
    mod = 10 ** y
    
    max_power = phi(mod)
    
    num = pow(x, max_power, mod)
    
    min_res = num
    for T in range(1, 86400):
        num = (num * x) % mod
        min_res = min(min_res, num)
    
    print(min_res)
    


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
