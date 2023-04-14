def parser():
    while 1:
        data = list(input().split(" "))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()

MOD = 10**9 + 7
LOG = 20


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def convert_to_tree(nodes, edges):
    tree = {n: 0 for n in range(nodes + 1)}
    graph = {n: [] for n in range(nodes + 1)}
    for node1, node2 in edges:
        tree[node2] = node1
        graph[node1].append(node2)
        graph[node2].append(node1)

    return tree, graph


def get_parents(tree, weights):
    parents = [[0] * LOG for _node in tree]
    # weights = [[1] * LOG for _node in tree]

    for node in tree:
        parents[node][0] = tree[node]
    for i in range(1, LOG):
        for node in tree:
            parents[node][i] = parents[parents[node][i - 1]][i - 1]
            # weights[node][i] = weights[node][i - 1] * weights[ parents[node][i - 1] ][i - 1] % MOD

    return parents
    # return parents, weights


def get_depth(graph, root):
    depths = [0] * len(graph)
    visited = [root]
    queue = [(root, 0)]
    while queue:
        x, depth = queue.pop(0)
        depths[x] = depth
        for child in graph[x]:
            if child not in visited:
                visited.append(child)
                queue.append((child, depth + 1))
    return depths


def get_lca(depth, parents, a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    k = depth[a] - depth[b] 

    for j in range(LOG - 1, -1, -1):
        if (k & (1<<j)):
            a = parents[a][j]
    # print(a, b, j, k)
    if a == b:
        return a
    
    for j in range(LOG - 1, -1, -1):
        if parents[a][j] != parents[b][j]:
            a = parents[a][j]
            b = parents[b][j]
    
    return parents[a][0]


def mod_inverse(n):
    return pow(n, MOD - 2, MOD)


def weights_to_ancestor(node, ancestor, tree, weights):
    total_weight = 1
    while node != ancestor:
        total_weight = total_weight * weights[node] % MOD
        node = tree[node]
    return total_weight * weights[node] % MOD


def solve():
    nodes = get_number()
    weights = [1] + [get_number() for _ in range(nodes)]
    edges = []
    edges = [(get_number(), get_number()) for _ in range(nodes - 1)]

    tree, graph = convert_to_tree(nodes, edges)
    # print(tree)

    parents = get_parents(tree, weights)
    # parents, binary_lift_weights = get_parents(tree, weights)
    # print(parents)
    for root, parent in tree.items():
        if parent == 0 and root != 0:
            break
    depth = get_depth(graph, root)
    # print(depth)
    q = get_number()
    for _ in range(q):
        t, u, v = get_number(), get_number() , get_number()
        
        if t == 1:
            weights[u] = v
        if t == 2:
            
            lca = get_lca(depth, parents, u, v)
            # print(lca)
            if lca == u:
                weight = weights_to_ancestor(v, u, tree, weights)
            elif lca == v:
                weight = weights_to_ancestor(u, v, tree, weights)
            else:
                weight = (
                    weights_to_ancestor(u, lca, tree, weights)
                    * weights_to_ancestor(v, lca, tree, weights)
                    * mod_inverse(weights[lca])
                    % MOD
                )
            print(weight)


def main():
    T = get_number()
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
