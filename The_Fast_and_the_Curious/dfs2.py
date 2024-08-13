import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


cycles = set()
from collections import defaultdict
parents = defaultdict(int)

def dfs_cycle(graph, start, parent, color):
    if color[start] == 1:
        current_node = parent
        cycles.add(current_node)
        while current_node != start:
            current_node = parents[current_node]
            cycles.add(current_node)
        return

    parents[start] = parent
    color[start] = 1
    for node in graph[start]:
        if node == parents[start] or color[node] == 2:
            continue
        dfs_cycle(graph, node, start, color)
    color[start] = 2
    
    return
    

def main():
    n, m = get_numbers()
    graph = defaultdict(list)
    for _ in range(m):
        u, v = get_numbers()
        graph[u].append(v)
        graph[v].append(u)
        
    color = [0] * (n + 1)
    dfs_cycle(graph, 1, -1, color)

    for node in graph:
        if node in cycles:
            continue
        print(node)  

if __name__ == '__main__':
    main()