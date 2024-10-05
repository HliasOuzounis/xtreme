# ---------------- Disjoint Set Union ---------------- #

# parents = [i for i in range(n)]   The root of the set each node belongs to
# sizes = [1] * n                   The size of each set

def find_root(parents, node):
    """
    Find the root of a node in a disjoint set
    """
    if parents[node] != node:
        parents[node] = find_root(parents, parents[node])
    return parents[node]

def union_sets(parents, sizes, a, b):
    """
    Union sets that contain a and b
    (a is the root of the new joint set)
    """
    a = find_root(a)
    b = find_root(b)

    if a != b:
        if sizes[a] < sizes[b]:
            a, b = b, a
        parents[b] = a
        sizes[a] += sizes[b]

