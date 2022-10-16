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

def find_sum():
    target_sum = get_number()
    list_len = get_number()
    nums = [get_number() for _ in range(list_len)]

    checked = set()
    for num in nums:
        if target_sum - num in checked:
            return f"{min(target_sum - num, num)} {max(target_sum - num, num)}"
        checked.add(num)
    return "!OK"


def main():
    T = get_number()
    for _ in range(T):
        print(find_sum())


if __name__ == "__main__":
    main()
