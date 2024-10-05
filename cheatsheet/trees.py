# ---------------- Trees ---------------- #


def get_depth_and_parents(graph, root):
    """
    Find the depth and parents of each node in a tree
    """
    depths = [0] * len(graph)
    parents = [0] * len(graph)

    visited = {root}
    queue = [(root, 0)]

    while queue:
        x, depth = queue.pop(0)
        depths[x] = depth

        for child in graph[x]:
            if child not in visited:
                parents[child] = x
                visited.add(child)
                queue.append((child, depth + 1))

    return depths, parents


def get_ancestors(graph, root, first_parents):
    """
    Find the ancestors of each node in a tree to use in binary lifting
    """
    from math import ceil, log2

    LOG = ceil(log2(len(graph)))
    parents = [[root] * LOG for node in graph]

    for node in graph:
        parents[node][0] = first_parents[node]
    for i in range(1, LOG):
        for node in graph:
            parents[node][i] = parents[parents[node][i - 1]][i - 1]
    return parents


def get_lca(depth, ancestors, a, b):
    """
    Lowest Common Ancestor (LCA) using binary lifting
    Needs a tree with parents and depths
    LOG = ceil(log2(n)) where n is the number of nodes in the tree
    """
    from math import ceil, log2

    LOG = ceil(log2(len(depth)))

    if depth[a] < depth[b]:
        a, b = b, a
    k = depth[a] - depth[b]

    for j in range(LOG - 1, -1, -1):
        if k & (1 << j):
            a = ancestors[a][j]

    if a == b:
        return a

    for j in range(LOG - 1, -1, -1):
        if ancestors[a][j] != ancestors[b][j]:
            a = ancestors[a][j]
            b = ancestors[b][j]

    return ancestors[a][0]