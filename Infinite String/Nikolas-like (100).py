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


def solve():
    letters = get_number()
    index = get_number()

    if letters == 1:
        return "a"

    block, rel_index = find_block(letters, index)

    num = rel_index // block
    string_pos = rel_index % block + 1

    return get_char(block, letters, num, string_pos)


def get_char(block, letters, num, string_pos):
    from string import ascii_lowercase

    mod1 = num % letters ** (block - string_pos + 1)
    mod2 = mod1 % letters ** (block - string_pos)
    char_id = (mod1 - mod2) // letters ** (block - string_pos)

    return ascii_lowercase[char_id]


def find_block(letters, index):
    """
    find which block the index refers to
    and get the relative index to the start of the block
    """
    block = 1
    block_size = letters * block
    while index > block_size:
        index -= block_size
        block += 1
        block_size = letters**block * block
    return block, index



def main():
    T = get_number()
    for _ in range(T):
        print(solve())


if __name__ == "__main__":
    main()
