# O(kdlog(k)) time, O(nm + k) space

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


def get_territories(grid, r, c):
    return sum(grid[r][:c+1])


def main():
    n, m = get_number(), get_number()
    k = get_number()
    grid = [[0 for _ in range(m)] for _ in range(n)]
    lions = [(get_number() - 1, get_number() - 1, get_number()) for _ in range(k)]


if __name__ == '__main__':
    main()
