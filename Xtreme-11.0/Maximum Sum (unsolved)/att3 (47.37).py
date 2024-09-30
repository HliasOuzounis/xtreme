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

import sys
sys.setrecursionlimit(10_000)

def best_seq(seq):
    sorted_seq = sorted(seq, reverse=True)
    best_seq = []
    for index, num in enumerate(sorted_seq):
        if index in (1, 0) or best_seq[0] <= best_seq[-1]:
            best_seq.append(num)
        else:
            best_seq.insert(0, num)
    best_seq = sort_smallest(best_seq, sorted_seq[0])
    print(sum_seq(best_seq))
    print_seq(best_seq)

def sort_smallest(seq, max_num):
    zero_count = 0

    while seq[-1] == 0:
        del seq[-1]
        zero_count += 1
    while seq[0] == 0:
        del seq[0]
        zero_count += 1

    index_max_num = seq.index(max_num)

    for i in range(len(seq)//2 + 1):
        if seq[i] < seq[-(i+1)]:
            break
        if seq[i] > seq[-(i+1)]:
            seq = seq[::-1]
            break
    
    for i in range(index_max_num):
        k = 1
        while seq[-k] < seq[i]:
            k += 1
        if seq[-k] == seq[i]:
            seq[i+1:-k] = sort_smallest(seq[i+1:-k], max_num)
            break
    
    return [0 for _ in range(zero_count)] + seq
    
def sum_seq(seq):
    if len(seq) == 1:
        return seq[0]
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
        best_seq(seq)


if __name__ == "__main__":
    main()