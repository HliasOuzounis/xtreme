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

def best_seq(seq):
    zeros = seq.count(0)
    ones = seq.count(1)
    l_array = []
    r_array = []
    seq = filter(lambda x: x not in (1, 0), seq)
    sorted_seq = sorted(seq, reverse=True)
    
    max_elem = sorted_seq[0]
    if ones >= 2:
        sorted_seq += [1, 1]
        ones -= 2
    elif ones == 1:
        sorted_seq.append(1)
        ones -= 1
        
    go_right = False
    for element in sorted_seq[1:]:
        if go_right:
            r_array.append(element)
        else:
            l_array.append(element)
        go_right = not go_right
    
    if len(r_array) >= len(l_array):
        final_array = r_array[::-1] + [max_elem] + l_array
    else:
        final_array = l_array[::-1] + [max_elem] + r_array
        
    final_array = [0] * zeros + [1] * ones + final_array
    
    return final_array, sum(final_array[i] * final_array[i + 1] for i in range(len(final_array) - 1))
        
    
def main():
    N = get_number()
    for _ in range(N):
        n = get_number()
        seq = [get_number() for _ in range(n)]
        seq, best_sum = best_seq(seq)
        print(best_sum)
        print(*seq)

if __name__ == "__main__":
    main()