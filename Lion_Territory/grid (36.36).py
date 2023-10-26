# O(k(d+m)) time, O(nm + k) space

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


def fill_grid(grid, n, m, lion_r, lion_c, d, go_up, go_down):
    if lion_r >= n or lion_r < 0:
        return
    if d < 0:
        return
    l_col = max(0, lion_c - d)
    grid[lion_r][l_col] += 1
    if lion_c + d + 1 < m:
        grid[lion_r][lion_c + d + 1] -= 1
    if go_down:
        fill_grid(grid, n, m, lion_r - 1, lion_c, d - 1, False, True)
    if go_up:
        fill_grid(grid, n, m, lion_r + 1, lion_c, d - 1, True, False)
    return


def get_territories(grid, r, c):
    return sum(grid[r][:c+1])


def main():
    n, m = get_number(), get_number()
    k = get_number()
    grid = [[0 for _ in range(m)] for _ in range(n)]
    lions = []
    for lion in range(k):
        r, c, d = get_number() - 1, get_number() - 1, get_number()
        fill_grid(grid, n, m, r, c, d, True, True)
        lions.append((r, c))
        
    max_lion, territories = max(((lion, get_territories(grid, r, c))
                                for lion, (r, c, ) in enumerate(lions, 1)), key=lambda x: x[1])
    # Lions are 1-indexed. The lion's own territory is also counted so we subtract it.
    print(max_lion, territories - 1)


if __name__ == '__main__':
    main()
