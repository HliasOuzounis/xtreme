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


def find_sum():  # sourcery skip: use-next
    target_sum = get_number()
    list_len = get_number()
    nums = [get_number() for _ in range(list_len)]

    end_index = None
    for index, num in enumerate(nums):
        if end_index is not None and index > end_index:
            break
        if target_sum - num in nums[index + 1 : end_index]:
            end_index = nums[index + 1 :].index(target_sum - num) + index + 1

    if end_index is None:
        return "!OK"
    num1 = nums[end_index]
    num2 = target_sum - num1
    return f"{min(num1, num2)} {max(num1, num2)}"


def main():
    T = get_number()
    for _ in range(T):
        print(find_sum())


if __name__ == "__main__":
    main()
