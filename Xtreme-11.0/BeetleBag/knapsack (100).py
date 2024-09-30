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


class Item:
    def __init__(self, weight, power) -> None:
        self.weight = weight
        self.power = power


def solve_case():
    capacity = get_number()
    n = get_number()
    items = [Item(0, 0)]
    for i in range(n):
        weight = get_number()
        power = get_number()
        items.append(Item(weight, power))
    sorted(items, key=lambda x: x.weight)

    knapsack_matrix = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            item = items[i]
            if item.weight > j:
                knapsack_matrix[i][j] = knapsack_matrix[i-1][j]
            else:
                knapsack_matrix[i][j] = max(
                    knapsack_matrix[i-1][j], knapsack_matrix[i-1][j-item.weight] + item.power)

    print(knapsack_matrix[n][capacity])


def main():
    t = get_number()
    for i in range(t):
        solve_case()


if __name__ == '__main__':
    main()