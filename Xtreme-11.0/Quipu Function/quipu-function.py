import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

maxN = 10**6
primes_sieve = [True] * (maxN + 1)
primes = []
def populate_primes():
    for i in range(2, maxN + 1):
        if primes_sieve[i]:
            for j in range(i*i, maxN + 1, i):
                primes_sieve[j] = False
            primes.append(i)

def get_total_divisors_range(a, b):
    factors = [[] for _ in range(b - a + 1)]
    
    for prime in primes:
        if prime > b:
            break
        
        smallest = a // prime * prime
        if smallest < a:
            smallest += prime
        
        while smallest <= b:
            idx = smallest - a
            factors[idx].append(0)
            
            n = smallest
            while n % prime == 0:
                factors[idx][-1] += 1
                n //= prime
            
            if n != 1:
                factors[idx].append(1)
                
            smallest += prime

    return factors


def solve_case(a: int, b: int, factors: list):
    d = get_number()
    s = 0
    for num in range(a, b+1):
        if num == d:
            s += 1
            continue
        
        divisors = 1
        for count in factors[num - a]:
            divisors *= count + 1
        
        count_d = 0
        while num % d == 0:
            count_d += 1
            num //= d
            
        s += divisors // (count_d + 1)
    
    print(s)


def main():
    total_cases, a, b = get_numbers()
    populate_primes()
    factors = get_total_divisors_range(a, b)
    for test_case in range(total_cases):
        solve_case(a, b, factors)


if __name__ == "__main__":
    main()
