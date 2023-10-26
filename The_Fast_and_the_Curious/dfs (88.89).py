import sys
sys.setrecursionlimit(10**6)

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

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

cycles = set()
from collections import defaultdict
parents = defaultdict(int)

def dfs_cycle(graph, start, parent, color):
    if color[start] == 2:
        return
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
        if node == parents[start]:
            continue
        dfs_cycle(graph, node, start, color)
    color[start] = 2
    return
    

def main():
    n, m = get_number(), get_number()
    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        u = get_number()
        v = get_number()
        graph[u].append(v)
        graph[v].append(u)
        
    color = [0] * (n + 1)
    for node in graph:
        dfs_cycle(graph, node, -1, color)
    for node in range(1, n+1):
        if node in cycles:
            continue
        print(node)  

if __name__ == '__main__':
    main()