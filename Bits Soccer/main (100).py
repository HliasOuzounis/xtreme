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


def check_roster(players, performance_index):
    curr_index = 0
    while players:
        player = players.pop()
        new_index = curr_index | player
        if not new_index & (~performance_index):
            curr_index = new_index
            if curr_index == performance_index:
                return "YES"
    return "NO"


def main():
    nof_players = get_number()
    players = [get_number() for _ in range(nof_players)]

    Q = get_number()
    for _ in range(Q):
        performance_index = get_number()
        print(check_roster(players.copy(), performance_index))


if __name__ == "__main__":
    main()
