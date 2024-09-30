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


def solve():
    nodes = get_number()
    node_weights = [0] + [get_number() for _weight in range(nodes)]
    adj = {node + 1: [] for node in range(nodes)}
    for _edge in range(nodes - 1):
        node1, node2 = get_number(), get_number()
        adj[node1].append(node2)
        adj[node2].append(node1)

    parents = [0] * (nodes + 1)
    depths = [0] * (nodes + 1)

    create_tree(1, adj, parents, depths)

    queries = get_number()
    for _query in range(queries):
        t, u, v = get_number(), get_number(), get_number()
        if t == 1:
            node_weights[u] = v
        else:
            answer_query(node_weights, u, v, parents, depths)


def create_tree(root, adj, parents, depth):
    for node in adj[root]:
        if node == parents[root]:
            continue
        parents[node] = root
        depth[node] = depth[root] + 1
        create_tree(node, adj, parents, depth)


def answer_query(weights, u, v, parents, depths):
    if depths[u] < depths[v]:
        u, v = v, u
    total_weights = 1
    while depths[u] > depths[v]:
        total_weights = total_weights * weights[u] % MOD
        u = parents[u]
    while u != v:
        total_weights = total_weights * weights[u] * weights[v] % MOD
        v = parents[v]
        u = parents[u]
    print(total_weights * weights[u] % MOD)


def main():
    test_cases = get_number()
    for _test in range(test_cases):
        solve()


if __name__ == "__main__":
    main()
