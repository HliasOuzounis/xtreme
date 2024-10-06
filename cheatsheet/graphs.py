# ---------------- Graphs ---------------- #

def bfs_shortest_path(graph, start_node, target_node):
    """
    Bfs implementation to find the shortest path between two nodes.
    Graph must not have weighted edges.

    returns distance between the nodes (-1 if they are not connected)
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


def dijkstra(graph, start_node):
    """
    Dijkstra's algorithm to find the shortest path from start_node to all other nodes
    Graph must be a dictionary with the following structure:
    graph = {node: [(neighbour, weight), ...]}
    """
    from heapq import heappush, heappop

    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    visited = set()
    queue = [(0, start_node)]

    while queue:
        dist, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                new_dist = dist + weight
                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    heappush(queue, (new_dist, neighbour))

    return distances


def has_cycle(graph):
    """
    Detect if a graph has a cycle
    """
    visited = [False] * len(graph)
    for start_node in graph:
        if start_node in graph[start_node]:
            # Self-loop
            return True
        if visited[start_node]:
            continue

        stack = [start_node]
        while stack:
            node = stack.pop(0)
            if visited[node]:
                return True
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    stack.append(neighbour)

    return False

def find_bridges(graph):
    """
    Find all the bridges in a graph
    Bridges are edges that when removed increase the number of connected components
    """
    from collections import defaultdict

    low = defaultdict(int)
    tin = defaultdict(int)
    timer = 0
    
    def dfs(node, parent, low, tin, timer):
        low[node] = tin[node] = timer
        timer += 1
        
        for child in graph[node]:
            if child == parent:
                continue
            
            if not tin[child]:
                timer = dfs(child, node, low, tin, timer)
                low[node] = min(low[node], low[child])
            else:
                low[node] = min(low[node], tin[child])
            
            if low[child] > tin[node]:
                ...
                # (node, child) is a bridge
        
        return timer
    
    for node in graph:
        if not tin[node]:
            timer = dfs(node, -1, low, tin, timer)