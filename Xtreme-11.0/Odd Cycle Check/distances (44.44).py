import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n = get_number()
    
    distances = [[float("inf")] * n for _ in range(n)]
    
    for i in range(n):
        distances[i][i] = 0
    
    while True:
        u, v = get_numbers()
        u -= 1
        v -= 1
        
        if distances[u][v] % 2 == 0:
            print(0, flush=True)
            sys.exit(0)

        distances[u][v] = 1
        distances[v][u] = 1
        
        for i in range(n):
            if distances[v][i] == float("inf") or i == u:
                continue
            for j in range(n):
                if distances[u][j] == float("inf") or j == v or j == i:
                    continue
                distances[i][j] = distances[v][i] + distances[u][j] + 1
                distances[j][i] = distances[i][j]
        
        print(1, flush=True)

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
