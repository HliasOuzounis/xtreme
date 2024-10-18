import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def update_range(rot_square, r1, c1, r2, c2):
    
    rot_square[r1][c1] += 1
    if c2 + 1 < len(rot_square[0]):
        rot_square[r1][c2 + 1] -= 1
    if r2 + 1 < len(rot_square):
        rot_square[r2 + 1][c1] -= 1
    if r2 + 1 < len(rot_square) and c2 + 1 < len(rot_square[0]):
        rot_square[r2 + 1][c2 + 1] += 1

def solve_case():
    n, m, k = get_numbers()
    swap = n > m
    if swap:
        n, m = m, n
    
    rot_square_size = m + n - 1
    rot_sqaure = [[0] * rot_square_size for _ in range(rot_square_size)]
    
    lions = []
    for k in range(k):
        ri, ci, di = get_numbers()
        lions.append((ri, ci))

        if swap:
            ri, ci = ci, ri
            
        new_r = m - 1 + ri - ci            
        new_c = ri + ci - 2        
            
        
        r1 = max(0, new_r - di)
        c1 = max(0, new_c - di)
        r2 = new_r + di
        c2 = new_c + di
        
        update_range(rot_sqaure, r1, c1, r2, c2)
        
    for i in range(1, rot_square_size):
        rot_sqaure[0][i] += rot_sqaure[0][i - 1]
    
    for i in range(1, rot_square_size):
        rot_sqaure[i][0] += rot_sqaure[i - 1][0]
        
        for j in range(1, rot_square_size):
            rot_sqaure[i][j] += rot_sqaure[i][j - 1] + rot_sqaure[i - 1][j] - rot_sqaure[i - 1][j - 1]
    

    best_score = 0
    best_lion = 0
    for i, (ri, ci) in enumerate(lions):
        if swap:
            ri, ci = ci, ri

        new_r = m - 1 + ri - ci
        new_c = ri + ci - 2
        
        score = rot_sqaure[new_r][new_c]
        
        if score > best_score:
            best_score = score
            best_lion = i
    
    print(best_lion + 1, best_score - 1)
    
def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
