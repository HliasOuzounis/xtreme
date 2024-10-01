def parser():
    while 1:
        data = list(input().split(" "))
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


MOD = 998_244_353


def comb_to_S(l, i, S, memo):
    if i >= len(l):
        return 1 if S == 0 else 0
    if (i, S) not in memo:

        a, b = l[i]
        count = sum(comb_to_S(l, i + 1, S - j * b, memo) % MOD for j in range(a + 1))

        memo[(i, S)] = count % MOD

    return memo[(i, S)]


def main():
    N = get_number()
    K = get_number()

    candies = [(get_number(), get_number()) for _ in range(N)]

    print(comb_to_S(candies, 0, K, {}))


if __name__ == "__main__":
    main()
