from math import log2


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


MOD = 10**9 + 7
LOG = int(log2(10) * 5)


def solve():
    nodes = get_number()
    weights = [0] + [get_number() for _weight in range(nodes)]
    edges = [(get_number(), get_number()) for _edge in range(nodes - 1)]

    tree = create_tree(edges, nodes)

    depths, parents = get_depth(tree, nodes)

    find_parents(parents, nodes)

    queries = get_number()
    for _query in range(queries):
        t, u, v = get_number(), get_number(), get_number()
        if t == 1:
            weights[u] = v
        else:
            answer_query(tree, weights, u, v, parents, depths)


def create_tree(edges, nodes):
    tree = {node + 1: [] for node in range(nodes)}

    for node1, node2 in edges:
        tree[node1].append(node2)
        tree[node2].append(node1)

    return tree


def get_depth(tree, nodes):
    depths = [0] * (nodes + 1)
    parents = [[]] + [[0] * LOG for _node in range(nodes)]

    root = 1
    parents[root][0] = root

    visited = [False] * (nodes + 1)
    queue = [(root, 0)]

    while queue:
        node, depth = queue.pop(0)
        if visited[node]:
            continue

        visited[node] = True
        depths[node] = depth

        for neighbour in tree[node]:
            if not visited[neighbour]:
                parents[neighbour][0] = node
                queue.append((neighbour, depth + 1))

    return depths, parents


def find_parents(parents, nodes):

    for j in range(1, LOG):
        for node in range(1, nodes + 1):
            parents[node][j] = parents[parents[node][j - 1]][j - 1]


def answer_query(tree, weights, u, v, parents, depths):
    lca = find_lca(parents, depths, u, v)
    total_weights = (
        weights_to_ancestor(weights, parents, lca, u)
        * weights_to_ancestor(weights, parents, lca, v)
        * weights[lca]
        % MOD
    )
    print(total_weights)


def find_lca(parents, depths, u, v):
    if depths[u] < depths[v]:
        u, v = v, u
    k = depths[u] - depths[v]

    j = 0
    while k:
        if k & 1:
            u = parents[u][j]
        j += 1
        k = k >> 1

    if u == v:
        return v

    for j in range(LOG - 1, -1, -1):
        if parents[u][j] != parents[v][j]:
            u = parents[u][j]
            v = parents[v][j]

    return parents[u][0]


def weights_to_ancestor(weights, parents, ancestor, node):
    prod = 1
    while node != ancestor:
        prod = prod * weights[node] % MOD
        node = parents[node][0]
    return prod


def main():
    test_cases = get_number()
    for _test in range(test_cases):
        solve()


if __name__ == "__main__":
    main()
