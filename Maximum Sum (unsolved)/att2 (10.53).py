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


def both_prepend(seq1, seq2, num):
    seq1.insert(0, num)
    seq2.insert(0, num)


def append_prepend(seq1, seq2, num):
    seq1.append(num)
    seq2.insert(0, num)


def max_sum(seq):
    sorted_seq = sorted(seq, reverse=True)
    append = True
    seq1, seq2 = [], []
    for index, num in enumerate(sorted_seq):
        if index == 0 or num == 0:
            both_prepend(seq1, seq2, num)
        elif seq1[0] == seq1[-1] and seq2[0] == seq2[-1] and index > 1:
            both_prepend(seq1, seq2, num)
        elif append:
            append_prepend(seq1, seq2, num)
            append = not append
        else:
            append_prepend(seq2, seq1, num)
            append = not append
    output(seq1, seq2)
    


def output(seq1, seq2):
    sum1 = sum_seq(seq1)
    sum2 = sum_seq(seq2)
    print(max(sum1, sum2))
    if sum1 > sum2:
        print_seq(seq1)
    elif sum2 > sum1:
        print_seq(seq2)
    else:
        print_seq(smallest_sequence(seq1, seq2))
    return


def smallest_sequence(seq1, seq2):
    for elem1, elem2 in zip(seq1, seq2):
        if elem1 > elem2:
            return seq2
        if elem2 > elem1:
            return seq1
    return seq1


def sum_seq(seq):
    return sum(seq[i] * seq[i + 1] for i in range(len(seq) - 1))


def print_seq(sequence):
    for num in sequence:
        print(num, end=" ")
    print()


def main():
    N = get_number()
    for _ in range(N):
        n = get_number()
        seq = [get_number() for _ in range(n)]
        max_sum(seq)


if __name__ == "__main__":
    main()
