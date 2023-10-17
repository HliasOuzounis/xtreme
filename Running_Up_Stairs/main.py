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

import sys
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(10**6)

cache = [0] * 22_001
def solve_case(steps):
    if cache[steps] != 0:
        return cache[steps]
    if steps == 0:
        return 1
    if steps == 1:
        return 1
    cache[steps] = solve_case(steps - 1) + solve_case(steps - 2)
    return cache[steps]
    

def main():
    t = get_number()
    for i in range(t):
        print(solve_case(steps := get_number()))
            

if __name__ == "__main__":
    main()