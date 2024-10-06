import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

MOD = 10**9 + 7
def solve_case():
    n = get_number()
    
    edges = []
    for _ in range(n - 1):
        u, v, w = get_numbers()
        edges.append((u, v, w))
    
    edges.sort(key=lambda x: x[2])
        
    roots = list(range(n + 1))
    sizes = [1] * (n + 1)
    
    total = 0
    for u, v, w in edges:
        u = find_root(roots, u)
        v = find_root(roots, v)
        
        total = (total + w * sizes[u] * sizes[v]) % MOD
        roots[v] = u
        sizes[u] += sizes[v]
    
    print(total)

def find_root(root, u):
    if root[u] != u:
        root[u] = find_root(root, root[u])
    return root[u]

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
