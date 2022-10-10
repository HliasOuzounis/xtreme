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


def prepend(array, elem):
    array.insert(0, elem)
    return


def smallest_sequence(seq1, seq2):
    for elem1, elem2 in zip(seq1, seq2):
        if elem1 > elem2:
            return seq2
        if elem2 > elem1:
            return seq1
    return seq1

def run_test():
    n = get_number()
    sequence = [get_number() for _ in range(n)]

    new_seq1 = []
    new_seq2 = []
    sums = [0, 0]
    first_right = n % 2
    # print("sorted: ", sorted(sequence, reverse=True))
    for num in sorted(sequence, reverse=True):
        if new_seq1 and (new_seq1[0] == new_seq1[-1] and len(new_seq1) > 1) or num == 0:
            sums[0] += num * new_seq1[0]
            sums[1] += num * new_seq2[0]

            prepend(new_seq1, num)
            prepend(new_seq2, num)

            # first_right = not first_right
            continue

        if first_right:
            if new_seq1:
                sums[0] += num * new_seq1[-1]
            new_seq1.append(num)

            if new_seq2:
                sums[1] += num * new_seq2[0]
            prepend(new_seq2, num)
        else:
            if new_seq2:
                sums[1] += num * new_seq2[-1]
            new_seq2.append(num)
            if new_seq1:
                sums[0] += num * new_seq1[0]
            prepend(new_seq1, num)

        first_right = not first_right
    
    if len(new_seq1) == 1:
        sums[0] = new_seq1[0]

    # print(new_seq1, new_seq2)
    if sums[1] == sums[0]:
        print(sums[0])
        print_seq(smallest_sequence(new_seq1, new_seq2))
    elif sums[1] > sums[0]:
        print(sums[1])
        print_seq(new_seq2)
    else:
        print(sums[0])
        print_seq(new_seq1)
    return
            

def print_seq(sequence):
    for num in sequence:
        print(num, end=" ")
    print()

def main():
    t = get_number()
    for _ in range(t):
        run_test()

if __name__ == "__main__":
    main()