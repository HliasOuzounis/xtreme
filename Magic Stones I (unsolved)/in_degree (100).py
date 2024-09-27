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

    querries = get_number()
    k = [get_number() for _ in range(querries)]

    count = [-1] * (n + 1)

    in_degree = [0] * (n + 1)
    for i in range(1, n + 1):
        in_degree[s[i]] += 1

    degree_dict = {i: set() for i in range(n + 1)}
    for i, deg in enumerate(in_degree):
        if i == 0:
            continue
        degree_dict[deg].add(i)

    total_stones = n

    moves = 1
    while True:
        if not degree_dict[0]:
            break
        total_stones -= len(degree_dict[0])
        for stone in degree_dict[0].copy():
            degree_dict[0].remove(stone)
            degree_dict[in_degree[s[stone]]].remove(s[stone])
            in_degree[s[stone]] -= 1
            degree_dict[in_degree[s[stone]]].add(s[stone])

        count[total_stones] = moves
        moves += 1

    for q in k:
        print(count[q])


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
