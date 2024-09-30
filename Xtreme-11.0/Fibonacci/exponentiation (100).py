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


def matrix_multiply(a, b):
    c = [[0, 0],
         [0, 0]]
    if not a or not b:
        return None
    assert len(a[0]) == len(b)
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                c[i][k] += a[i][j] * b[j][k]
                c[i][k] = c[i][k] % 10
    return c


def solve_case():
    fibonacci_matrix = [[1, 1], [1, 0]]
    n = get_number()
    sol = [[1, 0], [0, 1]]
    while n:
        if n % 2:
            sol = matrix_multiply(sol, fibonacci_matrix)
        fibonacci_matrix = matrix_multiply(fibonacci_matrix, fibonacci_matrix)
        n //= 2
    return sol[0][0]


def main():
    test_cases = get_number()
    for _ in range(test_cases):
        print(solve_case())


if __name__ == "__main__":
    main()
