# a simple parser for python. use get_number() and get_word() to read
from collections import defaultdict


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


bad_guys_dict = defaultdict(list)


def main():
    n = get_number()
    for bad_guy in range(n):
        name = get_word()
        height = get_number()
        bad_guys_dict[height].append(name)

    bad_guys = sorted(list(bad_guys_dict.items()), key=lambda x: x[0])

    total_bad_guys = 0
    for height, height_group in bad_guys:
        for name in sorted(height_group):
            print(name, end=' ')
        print(f"{total_bad_guys + 1} {total_bad_guys + len(height_group)}")
        total_bad_guys += len(height_group)


if __name__ == '__main__':
    main()
