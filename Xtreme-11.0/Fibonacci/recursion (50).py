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
sys.setrecursionlimit(1000000)
cache = {}
def calculate_fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: 
        cache[n] = (calculate_fibonacci(n-1) + calculate_fibonacci(n-2)) % 10
        return cache[n]
    
def solve_case(disaster_gen):
    print(calculate_fibonacci(disaster_gen))
    

def main():
    test_cases = get_number()
    for i in range(test_cases):
        solve_case(_disaster_gen := get_number())

if __name__ == '__main__':
    main()