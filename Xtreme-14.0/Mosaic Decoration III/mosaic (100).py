import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n, m, r, c = get_numbers()

    tiles = [get_numbers() for _ in range(r)]

    complete_tile_cost = sum(sum(tile) for tile in tiles)

    total_cost = 0
    
    mult_r, rem_n = divmod(n, r)
    mult_c, rem_m = divmod(m, c)
    
    total_cost += complete_tile_cost * (mult_r * mult_c)
    
    add_cost = float("inf")
    for start_x in range(50):
        if start_x > r:
            break
        for start_y in range(50):
            if start_y > c:
                break

            col_cost = 0
            for i in range(rem_m):
                i = (start_y + i) % c
                for j in range(r):
                    j = (start_x + j) % r
                    col_cost += tiles[j][i]
            row_cost = 0
            for i in range(rem_n):
                i = (start_x + i) % r
                for j in range(c):
                    j = (start_y + j) % c
                    row_cost += tiles[i][j]
            
            extra_cost = 0
            for i in range(rem_n):
                i = (start_x + i) % r
                for j in range(rem_m):
                    j = (start_y + j) % c
                    extra_cost += tiles[i][j]
            
            add_cost = min(add_cost, col_cost * mult_r + row_cost * mult_c + extra_cost)
    
    print(total_cost + add_cost)
            
def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
