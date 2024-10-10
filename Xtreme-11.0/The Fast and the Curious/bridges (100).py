import sys
sys.setrecursionlimit(10**6)


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    from collections import defaultdict
    n, m = get_numbers()

    graph = defaultdict(list)
    bridges = defaultdict(int)
    
    
    for _ in range(m):
        u, v = get_numbers()
        graph[u].append(v)
        graph[v].append(u)
        
    low = defaultdict(int)
    tin = defaultdict(int)
    timer = 1
    
    def dfs(node, parent, low, tin, timer):
        low[node] = tin[node] = timer
        timer += 1
        
        for child in graph[node]:
            if child == parent:
                continue
            
            if not tin[child]:
                timer = dfs(child, node, low, tin, timer)
                low[node] = min(low[node], low[child])
            else:
                low[node] = min(low[node], tin[child])
            
            if low[child] > tin[node]:
                bridges[node] += 1
                bridges[child] += 1
        
        return timer

    for node in graph:
        if not tin[node]:
            timer = dfs(node, -1, low, tin, timer)
    
    nodes = []
    for node in range(1, n + 1):
        if bridges[node] == len(graph[node]):
            nodes.append(node)
    
    for node in sorted(nodes):
        print(node)

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
