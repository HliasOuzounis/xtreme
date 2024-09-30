cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q","K", "A"]
def card_order(n):
    return cards.index(n)

def solve():
    player_A = input().split()
    player_B = input().split()
    
    game_state = set()
    while player_A and player_B:
        if (tuple(player_A), tuple(player_B)) in game_state:
            print("draw")
            return
        
        game_state.add((tuple(player_A), tuple(player_B)))
        card_a = player_A.pop(0)
        card_b = player_B.pop(0)
        if card_order(card_a) > card_order(card_b):
            player_A += [card_b]
        elif card_order(card_a) < card_order(card_b):
            player_B += [card_a]
        else:
            player_A += [card_a]
            player_B += [card_b]
    if player_A:
        print("player 1")
    if player_B:
        print("player 2")
        
    

def main():
    n = int(input())
    for _ in range(n):
        solve()

if __name__ == '__main__':
    main()