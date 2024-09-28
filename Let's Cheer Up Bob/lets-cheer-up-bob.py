import sys
from copy import deepcopy


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def check_win(grid, target=1):
    if any(all(grid[i][j] == target for i in range(3)) for j in range(3)):
        return True
    if any(all(grid[j][i] == target for i in range(3)) for j in range(3)):
        return True
    if all(grid[i][i] == target for i in range(3)):
        return True
    if all(grid[i][2 - i] == target for i in range(3)):
        return True
    
    return False
    
def solve_case():
    preferences = [get_numbers() for _ in range(9)]
    grid = [[0] * 3 for _ in range(3)]

    moves = dfs(grid, preferences, [], 0)
    for move in moves:
        print(*move)

def dfs(grid, preferences, moves, move_count):
    if check_win(grid, 2):
        return [(0, 0)] * 10
    
    for r, c in preferences:
        r -= 1
        c -= 1
        if not grid[r][c]:
            grid[r][c] = 1
            break

    if check_win(grid):
        return moves
    
    
    my_moves = [(0, 0)] * 9
    for r in range(3):
        for c in range(3):
            if not grid[r][c]:
                g = deepcopy(grid)
                g[r][c] = 2
                new_moves = dfs(g, preferences, moves + [(r + 1, c + 1)], move_count + 1)
                if len(my_moves) > len(new_moves):
                    my_moves = new_moves
                if len(my_moves) == len(new_moves):
                    for m1, m2 in zip(my_moves, new_moves):
                        if m1[0] < m2[0]:
                            break
                        if m1[0] > m2[0]:
                            my_moves = new_moves
                            break
                        if m1[1] < m2[1]:
                            break
                        if m1[1] > m2[1]:
                            my_moves = new_moves
                            break
    
    return my_moves


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
