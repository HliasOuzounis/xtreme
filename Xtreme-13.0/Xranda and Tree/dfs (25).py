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
    from collections import defaultdict
    n = get_number()

    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v, w = get_numbers()
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    print(sum(
        dfs(graph, root, root, -1, 0)
        for root in range(1, n + 1)
    ) // 2 % MOD)
        

import sys
sys.setrecursionlimit(10**6)
def dfs(graph, root, node, parent, dist):
    total = 0
    for child, w in graph[node]:
        if child == parent:
            continue
        new_dist = max(dist, w)
        total += new_dist + dfs(graph, root, child, node, new_dist)
    
    return total

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
