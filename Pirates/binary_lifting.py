# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
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


possible_moves = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1),            (0, 1),
                  (1, -1),   (1, 0),  (1, 1))

checked = set()
graph = {}


def get_matrix(sea_map):
    matrix = [[None for _ in range(len(sea_map[0]))]
              for _ in range(len(sea_map))]
    node = 0
    for i, row in enumerate(sea_map):
        for j, _cell in enumerate(row):
            if (i, j) in checked:
                continue
            if matrix[i][j] is None:
                dfs_find_connected(sea_map, matrix, (i, j), node)
                node += 1
    return matrix


def dfs_find_connected(sea_map, matrix, start, node):
    queue = [start]
    while queue:
        cell = queue.pop()
        if cell in checked:
            other_node = matrix[cell[0]][cell[1]]
            if other_node != node:
                if not node in graph:
                    graph[node] = set()
                graph[node].add(other_node)
                if not other_node in graph:
                    graph[other_node] = set()
                graph.get(other_node, set()).add(node)
            continue
        if sea_map[start[0]][start[1]] != sea_map[cell[0]][cell[1]]:
            continue
        checked.add(cell)
        matrix[cell[0]][cell[1]] = node
        for move in possible_moves:
            new_cell = (cell[0] + move[0], cell[1] + move[1])
            if new_cell[0] < 0 or new_cell[0] >= len(sea_map) or new_cell[1] < 0 or new_cell[1] >= len(sea_map[0]):
                continue
            queue.append(new_cell)


def get_depth(root):
    depths = [0] * len(graph)
    first_parents = [0] * len(graph)
    visited = {root}
    queue = [(root, 0)]
    while queue:
        x, depth = queue.pop(0)
        depths[x] = depth
        for child in graph[x]:
            if child not in visited:
                first_parents[child] = x
                visited.add(child)
                queue.append((child, depth + 1))
    return depths, first_parents


def get_parents(root, depths, first_parents):
    LOG = int(len(graph)**0.5 + 1)
    parents = [[root] * LOG for node in graph]

    for node in graph:
        parents[node][0] = first_parents[node]
    for i in range(1, LOG):
        for node in graph:
            parents[node][i] = parents[parents[node][i - 1]][i - 1]
    return parents


def answer_query(matrix, graph, parents, depths):
    start_x, start_y = get_number() - 1, get_number() - 1
    end_x, end_y = get_number() - 1, get_number() - 1
    start_node = matrix[start_x][start_y]
    end_node = matrix[end_x][end_y]

    if depths[start_node] < depths[end_node]:
        start_node, end_node = end_node, start_node
    depth_diff = depths[start_node] - depths[end_node]

    total_steps = 0
    LOG = int(len(graph)**0.5 + 1)
    for i in range(LOG - 1, -1, -1):
        if (depth_diff & (1 << i)):
            start_node = parents[start_node][i]
            total_steps += 2**i
    # Now start node and end node are on the same depth

    if start_node == end_node:
        print(total_steps//2)
        return

    for i in range(LOG - 1, -1, -1):
        if parents[start_node][i] != parents[end_node][i]:
            start_node = parents[start_node][i]
            end_node = parents[end_node][i]
            total_steps += 2**i * 2
    total_steps += 2
    assert parents[start_node][0] == parents[end_node][0]
    print(total_steps//2)


def main():
    n = get_number()
    m = get_number()
    queries = get_number()
    sea_map = []
    for i in range(n):
        map_row = get_word()
        sea_map.append([char == "~" for char in map_row])

    matrix = get_matrix(sea_map)
    root = matrix[n//2][m//2]
    depths, first_parents = get_depth(root)
    parents = get_parents(root, depths, first_parents)
    for q in range(queries):
        answer_query(matrix, graph, parents, depths)


if __name__ == '__main__':
    main()
