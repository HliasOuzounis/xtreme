# ------------------- GRAPHS ------------------- #


def visit_node(node):
    """
    Do something with node
    """
    return


def dfs_recursive(graph, vertex, visited):
    """
    Recursive dfs to traverse a graph.
    Used to detect cycles,

    graph: dictionary = {vertex: [neighbours, ]} -> adjecency list
    vertex: current vertex
    visited: boolean list (size = len(graph)) with previously visited nodes (True)
    """
    visit_node(vertex)
    visited[vertex] = True
    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs_recursive(graph, neighbour, visited)


def dfs_iter(graph, starting_vertex):
    """
    Iterative dfs to traverse a graph.
    Used to detect cycles,

    graph: dictionary = {vertex: [neighbours, ]} -> adjecency list
    starting_vertex: vertex to start the search, beware of disconnected graphs
    """
    visited = [False] * len(graph)
    stack = [starting_vertex]

    while stack:  # while stack not empty
        current_vertex = stack.pop()
        if not visited[current_vertex]:
            visit_node(current_vertex)
            visited[current_vertex] = True
            for neighbour in graph[current_vertex]:
                if not visited[neighbour]:
                    stack.append(neighbour)


def bfs_iter(graph, starting_vertex):
    """
    Iterative bfs to traverse a graph.
    Used to find shortest distance from node1 to node2,

    graph: dictionary = {vertex: [neighbours, ]} -> adjecency list
    starting_vertex: vertex to start the search, beware of disconnected graphs
    """
    visited = [False] * len(graph)
    queue = [starting_vertex]

    while queue:
        current_vertex = queue.pop(0)
        if not visited[current_vertex]:
            visit_node(current_vertex)
            visited[current_vertex] = True
            for neighbour in graph[current_vertex]:
                if not visited[neighbour]:
                    queue.append(neighbour)


def bfs_shortest_path(graph, start_node, target_node):
    """
    Bfs implementation to fins the shortest path between two nodes.
    Graph must not have weighted edges.

    returns distance between the nodes (-1 if they are npot connected)
            dictionary with the shortest path {node: previous node}
    """
    visited = [False] * len(graph)

    previous = {start_node: None}
    queue = [(start_node, 0)]

    while queue:
        current_node, dist = queue.pop(0)
        if not visited[current_node]:
            if current_node == target_node:
                return dist, previous

            visited[current_node] = True
            for neighbour in graph[current_node]:
                if not visited[neighbour]:
                    previous[neighbour] = current_node
                    queue.append((neighbour, dist + 1))

    return (-1, {})
