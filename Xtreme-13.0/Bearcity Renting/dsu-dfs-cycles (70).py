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

        graph = defaultdict(set)
        banned_edges = set()
        
        for u, v in edges:
            u = find_root(roots, u)
            v = find_root(roots, v)
            
            if u == v:
                banned_edges.add((u, u))
            
            if u in graph[v] and v in graph[u]:
                banned_edges.add((u, v))
                banned_edges.add((v, u))

            graph[u].add(v)
            graph[v].add(u)
            
        for u, v in edges:
            u = find_root(roots, u)
            v = find_root(roots, v)

            if (u, v) in banned_edges:
                continue
            
            graph[u].remove(v)
            graph[v].remove(u)

            ans += 1 - dfs(graph, u, -1, v, set())

            graph[u].add(v)
            graph[v].add(u)
            
            
        for u, v in edges:
            u = find_root(roots, u)
            v = find_root(roots, v)
            
            roots[v] = u

    print(ans)


def dfs(graph, start, parent, target, visited):
    if start == target:
        return True

    visited.add(start)
    for node in graph[start]:
        if node == parent or node in visited:
            continue
        if dfs(graph, node, start, target, visited.copy()):
            return True

    return False

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
