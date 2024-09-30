from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
# a simple parser for python. use get_number() and get_word() to read


def parser():
    while 1:
        data = list(input().split(" "))
        for number in data:
            if len(number) > 0:
                yield (number)


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


def main():
    n = get_number()
    q = get_number()
    graph = defaultdict(list)
    for i in range(n - 1):
        u = get_number()
        v = get_number()
        graph[u].append(v)
        graph[v].append(u)
    root = 0
    node_values = [0] * n
    
    import math
    log = int(math.log(n, 2) + 1)
    parents = [[-1] * log for i in range(n)]
    depths = [0] * n
    get_parents_and_depth(root, graph, parents, depths)
    fill_parents(parents, log)

    operations = ((get_number(), get_number(), get_number()) for i in range(q))
    for u, v, k in operations:
        perform_operation(u, v, k, node_values, parents, depths, log)
    
    for node in sorted(graph.keys(), key=lambda x: depths[x], reverse=True):
        if parents[node][0] != -1:
            node_values[parents[node][0]] += node_values[node]

    print(max(node_values))


def perform_operation(u, v, k, node_values, parents, depths, log):
    lca = get_lca(u, v, parents, depths, log)
    node_values[u] += k
    node_values[v] += k
    node_values[lca] -= k
    if parents[lca][0] != -1:
        node_values[parents[lca][0]] -= k


def get_parents_and_depth(root, graph, parents, depths):
    for node in graph[root]:
        if node == parents[root][0]:
            continue
        parents[node][0] = root
        depths[node] = depths[root] + 1
        get_parents_and_depth(node, graph, parents, depths)


def fill_parents(parents, log):
    for i in range(1, log):
        for j in range(len(parents)):
            if parents[j][i - 1] == -1:
                continue
            parents[j][i] = parents[parents[j][i - 1]][i - 1]


def get_lca(u, v, parents, depths, log):
    if depths[u] < depths[v]:
        u, v = v, u
    depth_diff = depths[u] - depths[v]
    for i in range(log - 1, -1, -1):
        if depth_diff & (1 << i):
            u = parents[u][i]
    if u == v:
        return u
    
    for i in range(log - 1, -1, -1):
        if parents[u][i] != parents[v][i]:
            u = parents[u][i]
            v = parents[v][i]
    return parents[u][0]


if __name__ == "__main__":
    main()
