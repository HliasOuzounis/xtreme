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


def get_adjecent(x, y, n, m):
    adjecent = []
    if x > 0:
        adjecent.append((x-1, y))
    if x < n-1:
        adjecent.append((x+1, y))
    if y > 0:
        adjecent.append((x, y-1))
    if y < m-1:
        adjecent.append((x, y+1))
    return adjecent


def main():
    n, m = get_number(), get_number()
    elevetion = [[get_number() for _ in range(m)] for _ in range(n)]
    water = [[1 for _ in range(m)] for _ in range(n)]

    from collections import defaultdict
    heights = defaultdict(list)
    for i, row in enumerate(elevetion):
        for j, cell in enumerate(row):
            heights[cell].append((i, j))

    sorted_heights = sorted(list(heights.items()),
                            key=lambda x: x[0], reverse=True)

    for height, cell_list in sorted_heights:
        for x, y in cell_list:
            adjecent_cells = get_adjecent(x, y, n, m)
            lower_cells = list(
                filter(lambda cell: elevetion[cell[0]][cell[1]] < height, adjecent_cells))
            if not lower_cells:
                continue
            split = water[x][y] / len(lower_cells)
            for cell in lower_cells:
                water[cell[0]][cell[1]] += split
                water[x][y] -= split

    max_water = 0
    for row in water:
        for cell in row:
            max_water = max(max_water, cell)
    print(max_water)


if __name__ == '__main__':
    main()
