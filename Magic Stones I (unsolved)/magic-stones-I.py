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
    s = get_numbers()

    querries = get_number()
    k = [get_number() for _ in range(querries)]

    count = [-1] * (n + 1)

    curr_set = set(i + 1 for i in range(n))

    move = 1
    while True:
        in_s = set(s[i - 1] for i in curr_set)
        if not curr_set - in_s:
            break

        count[len(in_s)] = move
        curr_set = in_s
        move += 1

    for q in k:
        print(count[q])


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
