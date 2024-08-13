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


def solve():
    dogs, walkers = get_number(), get_number()
    dog_sizes = sorted([get_number() for _ in range(dogs)])
    differences = sorted([dog_sizes[i+1] - dog_sizes[i] for i in range(dogs-1)])
    
    total_diff = dog_sizes[-1] - dog_sizes[0]
    # If we have a range a > b the differece is a - b.
    # If we split the range at c > d the difference becomes a - c + d - b = a - b - (c - b).
    for walker in range(1, walkers):
        total_diff -= differences.pop(0)
    print(total_diff)
    

def main():
    t = get_number()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()