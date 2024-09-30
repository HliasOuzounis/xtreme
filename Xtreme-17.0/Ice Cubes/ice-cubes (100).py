# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def solve(case_num):
    N, M, K, B = get_number(), get_number(), get_number(), get_number()
    grid = [[get_number() for _ in range(M)] for _ in range(N)]
    best_route = [[[-1] * (K + 1) for _ in range(M)] for _ in range(N)]

    best_route[0][0][grid[0][0] < B] = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] >= B:
                is_in_valid_path = (i == 0 and j == 0)
                if i > 0:
                    if not all([x == -1 for x in best_route[i - 1][j]]):
                        best_route[i][j][0] = max(best_route[i - 1][j])
                        is_in_valid_path = True
                if j > 0:
                    if not all([x == -1 for x in best_route[i][j - 1]]):
                        best_route[i][j][0] = max(
                            best_route[i][j][0], max(best_route[i][j - 1]))
                        is_in_valid_path = True
                best_route[i][j][0] += grid[i][j] if is_in_valid_path else 0
            else:
                for k in range(1, K):
                    is_in_valid_path = (i == 0 and j == 0 and k == 1)
                    if i > 0:
                        if best_route[i - 1][j][k - 1] >= 0:
                            best_route[i][j][k] = best_route[i - 1][j][k - 1]
                            is_in_valid_path = True
                    if j > 0:
                        if best_route[i][j - 1][k - 1] >= 0:
                            best_route[i][j][k] = max(
                                best_route[i][j][k], best_route[i][j - 1][k - 1])
                            is_in_valid_path = True
                    best_route[i][j][k] += grid[i][j] if is_in_valid_path else 0

    max_route = max(best_route[-1][-1])
    if max_route == -1:
        print(f"Case {case_num}: IMPOSSIBLE")
    else:
        print(f"Case {case_num}: {max_route}")


def main():
    T = get_number()
    for case in range(T):
        solve(case + 1)


if __name__ == "__main__":
    main()
