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
    distances = {node: float('inf') for node in graph}
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
        if (k & (1<<j)):
            a = ancestors[a][j]
    
    if a == b:
        return a
    
    for j in range(LOG - 1, -1, -1):
        if ancestors[a][j] != ancestors[b][j]:
            a = ancestors[a][j]
            b = ancestors[b][j]
    
    return ancestors[a][0]

# ---------------- Integers ---------------- #


def all_common_divisors(n1, n2):
    """
    Generator that returns all common divisors of two numbers in descending order (except 1)
    """
    if n2 % n1 == 0:
        yield n1
    n1, n2 = min(n1, n2), max(n1, n2)
    for i in range(int(n1 // 2) + 1, 1, -1):
        if n1 % i == 0 and n2 % i == 0:
            yield i


def gcd_Euclid(a, b):
    """
    returns the greatest common divisor of two numbers a, b (a < b)
    """
    if b == 0:
        return a
    return gcd_Euclid(b, a % b)

def fast_expontiation(base, exp, mod):
    """
    Fast exponentiation algorithm to calculate base**exp % mod
    equivilant to pow(base, exp, mod) in python
    but can be used for matrices and other types
    """
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def smallest_divisible(n, p):
    """
    Find the smallest number x (x > n) that is divisible by p
    """
    smallest = n // p * p
    if smallest < n:
        smallest += p
    return smallest

def xor_range(x):
    """
    Calculate the xor of all numbers from 0 to x
    """
    match x % 4:
        case 0:
            return x
        case 1:
            return 1
        case 2:
            return x + 1
        case _:
            return 0

# ---------------- Primes ---------------- #

def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n
    """
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return primes

# ---------------- Modulo ---------------- #
# https://sites.math.washington.edu//~greenber/Congruences.pdf

MOD = 998244353
MOD = 10**9 + 7


def mod_inverse_prime(a):
    """
    Get the modular inverse of a assuming mod is prime
    using Fermat's little theorem
    a**(p-1) = 1 mod p
    """
    # Python's pow method returns base**exp % mod
    return pow(base=a, exp=MOD - 2, mod=MOD)


def nCr_with_mod(n, r):
    """
    Efficiently calculate nCr(n, r) % mod, mod is prime
    """
    r = min(r, n - r)

    numerator = 1
    denominator = 1

    for i in range(r):
        numerator = (numerator * (n - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD

    return (numerator * mod_inverse_prime(denominator)) % MOD

# ----------------- STRINGS ----------------- #

def lexicographically_smaller(a, b):
    """
    Check if iterable a is lexicographically smaller than b
    """
    for ai, bi in zip(a, b):
        if ai > bi:
            return False
        if ai < bi:
            return True
    
    return len(a) <= len(b)