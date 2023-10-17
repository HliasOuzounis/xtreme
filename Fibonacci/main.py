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


pattern = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9,
           0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]
pattern_len = len(pattern) - 1
# -1 beacause the true pattern cycles after 9, 1 but we add a 0 to avoid index errors (if disaster_gen % pattern_len == 59)


def solve_case(disaster_gen):
    print(pattern[disaster_gen % pattern_len + 1])


def main():
    test_cases = get_number()
    for i in range(test_cases):
        solve_case(_disaster_gen := get_number())


if __name__ == '__main__':
    main()
