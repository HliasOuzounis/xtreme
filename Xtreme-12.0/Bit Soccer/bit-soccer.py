import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def check_team(player_index, qi):
    running_index = 0
    for player in player_index:
        if player & (~qi) != 0:
            continue
        
        running_index = running_index | player
        if running_index == qi:
            return True
        
    return False


def solve_case():
    n = get_number()
    player_index = get_numbers()
    
    q = get_number()
    for _ in range(q):
        qi = get_number()
        
        print("YES" if check_team(player_index, qi) else "NO")
    

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
