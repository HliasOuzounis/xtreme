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

# from functools import cache
# import functools

INF = 999999999
moves = {"D": (1, 0), "L": (0, -1), "R": (0, 1), "U": (-1, 0)}

 
def complete_bfs(table, pacman_pos, ghosts):
    ghost_visited = []
    pacman_visited = []
    distances = dict()
    paths = dict()
    queue = [(pacman_pos, INF, "", True)] + [(ghost, 0, "", False) for ghost in ghosts]
    while queue:
        pos, distance, path, is_pacman = queue.pop(0)
        if pos in ghost_visited:
            continue
        if is_pacman and pos in pacman_visited:
            continue
        if is_pacman:
            distances[pos] = INF
            paths[pos] = path
        elif pos in distances:
            distances[pos] = distance
        if is_pacman:
            pacman_visited.append(pos)
        else:
            ghost_visited.append(pos)

        for move in moves.keys():
            d_row, d_col = moves[move]
            neighbour = (pos[0] + d_row, pos[1] + d_col)
            if not table[pos[0] + d_row][pos[1] + d_col]:
                continue
            if is_pacman and neighbour not in pacman_visited:
                queue.append((neighbour, INF, path + move, True))
            elif not is_pacman and neighbour not in ghost_visited:
                queue.append((neighbour, distance + 1, "", False))
    return distances, paths


def main():
    t = get_number()
    for tests in range(t):
        rows, cols = get_number(), get_number()
        table = [[0 for _col in range(cols + 2)] for _row in range(rows + 2)]
        ghosts = []
        for row in range(rows):
            table_row = get_word()
            for col, char in enumerate(table_row):
                if char == "G":
                    table[row + 1][col + 1] = 1
                    ghosts.append((row + 1, col + 1))
                elif char == "P":
                    table[row + 1][col + 1] = 1
                    pacman_pos = (row + 1, col + 1)
                elif char == ".":
                    table[row + 1][col + 1] = 1

        distances, paths = complete_bfs(table, pacman_pos, ghosts)
        max_distance = max(distances.values())
        candidate_squares = [
            square for square in distances if distances[square] == max_distance
        ]
        min_lex = min(pos[0] for pos in candidate_squares)
        candidate_squares = [pos for pos in candidate_squares if pos[0] == min_lex]
        min_lex = min(pos[1] for pos in candidate_squares)
        candidate_squares = [pos for pos in candidate_squares if pos[1] == min_lex]

        best_sqaure = candidate_squares[0]
        distance_from_ghosts = distances[best_sqaure]
        pacman_path = paths[best_sqaure]
        if distance_from_ghosts == INF:
            distance_from_ghosts = "INFINITE"
        else:
            distance_from_ghosts -= 1
        if not pacman_path:
            pacman_path = "STAY"
        print(f"Case #{tests + 1}: {distance_from_ghosts}", pacman_path)


if __name__ == "__main__":
    main()