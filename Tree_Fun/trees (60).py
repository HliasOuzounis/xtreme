import sys
sys.setrecursionlimit(10**6)
# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(" "))
        for number in data:
            if len(number) > 0:
                yield (number)


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

from collections import defaultdict
def convert_to_adjecency_list(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def main():
    n = get_number()
    q = get_number()
    edges = [(get_number(), get_number()) for i in range(n - 1)]
    operations = [(get_number(), get_number(), get_number()) for i in range(q)]
    graph = convert_to_adjecency_list(edges)
    
    root = 0
    node_values = [0] * n
    parents = [root] * n
    depths = [0] * n
    get_parents_and_depth(root, graph, parents, depths)
            
    for u, v, k in operations:
        if u == v:
            node_values[u] += k
            continue
        if depths[u] < depths[v]:
            u, v = v, u
        
        node_values[u] += k
        node_values[v] += k
                
        while depths[u] > depths[v]:
            u = parents[u]
            if u != v:
                node_values[u] += k
        
        while u != v:
            u = parents[u]
            v = parents[v]
            if u != v:
                node_values[u] += k
                node_values[v] += k
            else:
                node_values[u] += k
    
    print(max(node_values))
            

def get_parents_and_depth(root, graph, parents, depths):
    for node in graph[root]:
        if node == parents[root]:
            continue
        parents[node] = root
        depths[node] = depths[root] + 1
        get_parents_and_depth(node, graph, parents, depths)

    

if __name__ == "__main__":
    main()