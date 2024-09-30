import sys
sys.setrecursionlimit(1000000)
from functools import cache
@cache
def calculate_fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: 
        return (calculate_fibonacci(n-1) + calculate_fibonacci(n-2)) % 10

def main():
    sequence = [calculate_fibonacci(i) for i in range(1_000)]
    tuples = set()
    for i in range(1000 - 1):
        adj = tuple(sequence[i:i+2])        
        if adj in tuples:
            print(i)
            print(sequence[:i+1])
            break
        else:
            tuples.add(adj)

if __name__ == "__main__":
    main()