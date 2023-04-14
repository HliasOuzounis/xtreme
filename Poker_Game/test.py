import random
from Poker_Game import card_priorities, main

possible_cards = {'2' : 4, '3' : 4, '4' : 4, '5' : 4, '6' : 4, '7' : 4, 
                    '8' : 4, '9' : 4, 'X' : 4, 'J' : 4, 'Q' : 4, 'K' : 4, 'A' : 4}
seq = "23456789XJQKA"
k = random.randint(2,8)
hand = random.choices(seq, k = k)
hand = "".join(sorted([c for c in hand], key= lambda x: card_priorities(x)))

print(hand)

played_cards = ""
actions = []
n = random.randint(3, 50 - k)
for i in range(n):
    card = random.choice(seq)
    if card in played_cards or card in hand:
        actions.append(True)
    else:
        actions.append(False)
    played_cards += card
print(played_cards)
for a in actions:
    if a: print("y", end="")
    else: print("n", end="")
print()
print(main(n, k, played_cards, actions))
