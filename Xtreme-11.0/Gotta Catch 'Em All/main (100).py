# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

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


def main():
    r, c = get_number(), get_number()
    forest = [[get_number() for _ in range(c)] for _ in range(r)]
    health_matrix = [[float("inf") for _ in range(c)] for _ in range(r)]
    health_matrix[r - 1][c - 1] = 1
    for i in range(r - 1, -1, -1):
        for j in range(c - 1, -1, -1):
            health_matrix[i][j - 1] = min(max(health_matrix[i][j] - forest[i][j - 1], 1), health_matrix[i][j - 1])
            health_matrix[i - 1][j] = min(max(health_matrix[i][j] - forest[i - 1][j], 1), health_matrix[i - 1][j])
    print(health_matrix[0][0])


if __name__ == '__main__':
    main()