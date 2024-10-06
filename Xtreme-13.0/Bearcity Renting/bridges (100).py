import sys
sys.setrecursionlimit(10**6)


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def find_root(roots, node):
    if roots[node] != node:
        roots[node] = find_root(roots, roots[node])
    return roots[node]


def solve_case():
    n, m = get_numbers()
    edges = []
    for _ in range(m):
        u, v, w = get_numbers()
        edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])

    edge_sizes = []
    prev_size = (0, [])
    for u, v, w in edges:
        if w == prev_size[0]:
            prev_size[1].append((u, v))
        else:
            if prev_size[1]:
                edge_sizes.append(prev_size)
            prev_size = (w, [(u, v)])

    if prev_size[1]:
        edge_sizes.append(prev_size)

    roots = list(range(n + 1))
    sizes = [1] * (n + 1)
    
    ans = 0
    for edge_size, edges in edge_sizes:
        from collections import defaultdict

        graph = defaultdict(lambda: defaultdict(int))
        
        for u, v in edges:
            u = find_root(roots, u)
            v = find_root(roots, v)
            
            if u == v:
                continue
            
            graph[u][v] += 1
            graph[v][u] += 1
            
        tin = defaultdict(int)
        low = defaultdict(int)
        timer = 1
        
        for node in graph:
            if not tin[node]:
                res = dfs(graph, node, -1, low, tin, timer)
                ans += res[0]
                timer = res[1]
            
        for u, v in edges:
            u = find_root(roots, u)
            v = find_root(roots, v)
            
            roots[v] = u

    print(ans)

def dfs(graph, node, parent, low, tin, timer):
    low[node] = tin[node] = timer
    timer += 1
    
    ans = 0
    for child in graph[node].keys():
        if child == parent:
            continue
        
        if tin[child]:
            low[node] = min(low[node], tin[child])
        else:
            res = dfs(graph, child, node, low, tin, timer)
            ans += res[0]
            timer = res[1]
            low[node] = min(low[node], low[child])
            if low[child] > tin[node] and graph[node][child] == 1:
                ans += 1
                
    return ans, timer


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
