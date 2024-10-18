import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def update(fwk, x, y, v):
    x += 1
    y += 1
    
    while x < len(fwk):
        yf = y
        while yf < len(fwk[x]):
            fwk[x][yf] += v
            yf += yf & -yf
        
        x += x & -x
    return fwk

def update_range(fwk, r1, c1, r2, c2):
    r1 += 1
    c1 += 1
    r2 += 1
    c2 += 1
    
    update(fwk, r2, c2, 1)
    if r1 > 0:
        update(fwk, r1 - 1, c2, -1)
    if c1 > 0:
        update(fwk, r2, c1 - 1, -1)
    if r1 > 0 and c1 > 0:
        update(fwk, r1 - 1, c1 - 1, 1)


def query(fwk, x, y):
    x += 1
    y += 1
    
    s = 0
    while x > 0:
        yf = y
        while yf > 0:
            s += fwk[x][yf]
            yf -= yf & -yf
        
        x -= x & -x
    
    return s

def solve_case():
    n, m, k = get_numbers()
    swap = n > m
    if swap:
        n, m = m, n
    
    
    rot_square_size = m + n
    fwk = [[0] * rot_square_size for _ in range(rot_square_size)]
    
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
        r2 = min(rot_square_size - 1, new_r + di)
        c2 = min(rot_square_size - 1, new_c + di)
        
        update_range(fwk, r1, c1, r2, c2)
    

    best_score = 0
    best_lion = 0
    for i, (ri, ci) in enumerate(lions):
        if swap:
            ri, ci = ci, ri

        new_r = m - 1 + ri - ci
        new_c = ri + ci - 2
        
        score = query(fwk, new_r, new_c)
        
        if score > best_score:
            best_score = score
            best_lion = i
    
    print(best_lion + 1, best_score - 1)
    
def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
