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


def main():
    treat_score = {}
    m = get_number()

    for _meal in range(m):
        payer = get_word()
        meals = get_number()
        treat_score[payer] = treat_score.setdefault(payer, 0) - meals
        for _payees in range(meals):
            payee = get_word()
            treat_score[payee] = treat_score.setdefault(payee, 0) + 1

    print(
        sum(amount for amount in treat_score.values() if amount > 0),
        -min(amount for amount in treat_score.values() if amount < 0),
    )
    


if __name__ == "__main__":
    t = get_number()
    for _ in range(t):
        main()
