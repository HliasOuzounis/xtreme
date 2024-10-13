import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


moves = ((1, 0), (0, -1), (0, 1), (-1, 0))
move_str = "DLRU"

def solve_case(test_case):
    n, m = get_numbers()
    table = [[0] * m for _ in range(n)]

    pacman_pos = None
    ghosts_pos = []
    
    for i in range(n):
        row = get_word()
        for j, cell in enumerate(row):
            table[i][j] = cell != "X"
            if cell == "P":
                pacman_pos = (i, j)
            elif cell == "G":
                ghosts_pos.append((i, j))
    
    survival, best_path = bfs(table, pacman_pos, ghosts_pos)
    
    best_pos = None
    max_surv = -float("inf")
    for i in range(n):
        for j in range(m):
            if survival[i][j] > max_surv:
                max_surv = survival[i][j]
                best_pos = (i, j)
    max_surv -= 1
    
    print(f"Case #{test_case + 1}:", end=" ")
    
    if max_surv == float("inf"):
        print("INFINITE", end=" ")
    else:
        print(max_surv, end=" ")
    
    if best_pos == pacman_pos:
        print("STAY")
        return
    
    print(best_path[best_pos])
   

def bfs(table, pacman_pos, ghost_pos):
    from collections import deque, defaultdict
    
    pacman_visited = set()
    ghost_visited = set()
    
    survival = [[-float("inf")] * len(table[0]) for _ in range(len(table))]
    best_path = defaultdict(str)
    
    queue = deque([(ghost, 0, False, "") for ghost in ghost_pos] + [(pacman_pos, 0, True, "")])
    while queue:
        pos, dist, is_pacman, path = queue.popleft()
        if pos in ghost_visited:
            continue
        if is_pacman and pos in pacman_visited:
            continue
        if is_pacman:
            best_path[pos] = path
            pacman_visited.add(pos)
            if pos not in ghost_visited:
                survival[pos[0]][pos[1]] = float("inf")
        else:
            ghost_visited.add(pos)
            if pos in pacman_visited:
                survival[pos[0]][pos[1]] = dist
        
        for i, (dy, dx) in enumerate(moves):
            new_pos = (pos[0] + dy, pos[1] + dx)
            if new_pos[0] < 0 or new_pos[0] >= len(table) or new_pos[1] < 0 or new_pos[1] >= len(table[0]):
                continue
            if not table[new_pos[0]][new_pos[1]]:
                continue
            
            queue.append((new_pos, dist + 1, is_pacman, path + move_str[i]))
    
    return survival, best_path


def main():
    for test_case in range(total_cases := get_number()):
        solve_case(test_case)


if __name__ == "__main__":
    main()
