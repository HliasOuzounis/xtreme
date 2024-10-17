import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def union(roots, u, v):
    u1 = find(roots, u * 2)
    u2 = find(roots, u * 2 + 1)
    v1 = find(roots, v * 2)
    v2 = find(roots, v * 2 + 1)
    
    roots[u1] = roots[v2]
    roots[u2] = roots[v1]
    
def find(roots, u):
    if roots[u] != u:
        roots[u] = find(roots, roots[u])
    return roots[u]

def solve_case():
    n = get_number()
    
    roots = list(range(2 * n))
    while True:
        u, v = get_numbers()
        u -= 1
        v -= 1
        
        if find(roots, 2 * u) == find(roots, 2 * v):
            print(0, flush=True)
            sys.exit(0)
        if find(roots, 2 * u + 1) == find(roots, 2 * v + 1):
            print(0, flush=True)
            sys.exit(0)
        
        union(roots, u, v)        
        print(1, flush=True)

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
