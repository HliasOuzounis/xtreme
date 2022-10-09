def has_cycle(graph):
    visited = [False] * len(graph)
    for start_node in graph:
        if visited[start_node]:
            continue
        stack = [start_node]
        while stack:
            node = stack.pop(0)
            if visited[node] or node in graph[node]:
                return True
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    stack.append(neighbour)
    return False


def main():
    vertices, edges = tuple(map(int, input().split()))
    edges_input = tuple(map(int, input().split()))
    edges = (
        (edges_input[i], edges_input[i + 1]) for i in range(0, len(edges_input), 2)
    )
    graph = {i: [] for i in range(vertices)}
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    if has_cycle(graph):
        print("1")
    else:
        print("0")


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        main()
