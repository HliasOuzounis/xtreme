# O(k^2) time, O(k) space
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


class Lion:
    def __init__(self, idx, x, y, d) -> None:
        self.idx = idx + 1
        self.x = x
        self.y = y
        self.d = d
        self.in_territories = 0


def main():
    n, m = get_number(), get_number()
    k = get_number()
    lions = [Lion(idx, get_number(), get_number(), get_number())
             for idx in range(k)]
    for idx, lion in enumerate(lions):
        for other_lion in lions[idx+1:]:
            distance = abs(lion.x - other_lion.x) + abs(lion.y - other_lion.y)
            if distance <= lion.d:
                other_lion.in_territories += 1
            if distance <= other_lion.d:
                lion.in_territories += 1
    lions = sorted(lions, key=lambda x: x.in_territories, reverse=True)
    print(lions[0].idx, lions[0].in_territories)


if __name__ == '__main__':
    main()
