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
    
    while x < len(fwk):
        fwk[x][y] += v
        x += x & -x

def update_range(fwk, x, l, r, v):
    update(fwk, l, x, v)
    update(fwk, r + 1, x, -v)

def query(fwk, x, y):
    x += 1
    
    s = 0
    while x > 0:
        s += fwk[x][y]
        x -= x & -x
    
    return s

def solve_case():
    n, m, k = get_numbers()
    
    lions = [get_numbers() for _ in range(k)]
    
    fwk = [[0] * (m + 1) for _ in range(n + 1)]
    
    for ri, ci, di in lions:
        ri -= 1
        ci -= 1
        
        for i in range(di + 1):
            if ci - i < 0:
                break
            
            ri1 = max(0, ri - di + i)
            ri2 = min(n, ri + di - i)
            
            update_range(fwk, ci - i, ri1, ri2, 1)
        
        for i in range(1, di + 1):
            if ci + i >= m:
                break
            
            ri1 = max(0, ri - di + i)
            ri2 = min(n, ri + di - i)
            
            update_range(fwk, ci + i, ri1, ri2, 1)
            
    best_lion = None
    best_score = 0
    for i, (ri, ci, _) in enumerate(lions):
        ri -= 1
        ci -= 1
        score = query(fwk, ri, ci)
        if score > best_score:
            best_score = score
            best_lion = i
    print(best_lion + 1, best_score - 1)
            


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
