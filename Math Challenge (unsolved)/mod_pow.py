# a simple parser for python. use get_number() and get_word() to read
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


MOD = 10**9 + 7


def calculate_power(a, power):
    return pow(a, power, MOD)


def mod_inverse(a, p):
    return pow(a, p - 2, p)


def nCr_with_mod(n, r, mod):
    r = min(r, n - r)

    numerator = 1
    denominator = 1

    for i in range(r):
        numerator = numerator * (n - i) % mod
        denominator = denominator * (i + 1) % mod
    

    return numerator * mod_inverse(denominator, mod) % (MOD - 1)


def main():
    T = get_number()
    for _ in range(T):
        a, b, c = get_number(), get_number(), get_number()
        if a == 1:
            print("1")
            continue
        power = nCr_with_mod(b, c, (MOD - 1)//2)
        print(calculate_power(a, power))


if __name__ == "__main__":
    main()
