import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


cut = (0, 0)


def subtree_sizes(graph, node, parent, sizes, parents, depths, curr_depth):
    sizes[node] = 1
    parents[node] = parent
    depths[node] = curr_depth

    for child in graph[node]:
        if child == parent:
            continue

        subtree_sizes(graph, child, node, sizes, parents, depths, curr_depth + 1)
        sizes[node] += sizes[child]


def print_nodes_of_subtree(graph, node, parent):
    print(f"flip {node}")
    for child in graph[node]:
        if child == parent:
            continue
        print_nodes_of_subtree(graph, child, node)


def solve_case():
    from collections import defaultdict

    n, k = get_numbers()

    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = get_numbers()
        graph[u].append(v)
        graph[v].append(u)

    sizes = [0] * (n + 1)
    parents = [0] * (n + 1)
    depths = [0] * (n + 1)

    subtree_sizes(graph, 1, 0, sizes, parents, depths, 0)

    cut = (0, 0)
    for node in range(1, n + 1):
        # subtree1 has k1 blue nodes, subtree2 has k - k1 blue nodes
        # After flip subtree1 has m - k1 blue nodes where m is the size of subtree1
        # If m == k => m - k1 == k - k1
        if sizes[node] == k or sizes[node] == n - k:
            cut = (node, parents[node])

    if 0 in cut:
        print(-1)
        return

    print_nodes_of_subtree(graph, cut[0], cut[1])
    print(f"cut {cut[0]} {cut[1]}")


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
