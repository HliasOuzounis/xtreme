def card_priorities(x):
        return "23456789XJQKA".index(x)

def main(n, k, played_cards, actions):
    certain_cards = set()
    possible_cards = {'2' : 4, '3' : 4, '4' : 4, '5' : 4, '6' : 4, '7' : 4, 
                    '8' : 4, '9' : 4, 'X' : 4, 'J' : 4, 'Q' : 4, 'K' : 4, 'A' : 4}

    for i, card in enumerate(played_cards):
        if not actions[i]: # n
            if card in possible_cards:
                del possible_cards[card]  
            if card in played_cards[:i]:
                return "impossible"
        else: # y
            if card in possible_cards:
                possible_cards[card] -= 1
            if card in played_cards[:i]:
                continue # y because it was seen previously
            certain_cards.add(card)

    print(possible_cards)
    print(certain_cards)

    if (not possible_cards or len(certain_cards) > k or 
    sum((val for val in possible_cards.values())) < k - len(certain_cards)
    or any(val <= 0 for val in possible_cards.values())): # if there aren't enough possible cards or a card has had 4+ y
        return "impossible"

    hand = "".join((card for card in certain_cards))
    for card in hand:
        if card in possible_cards:
            possible_cards[card] -= 1 # remove certain cards from possible 
    # sort by seen most (closer to 4 of a kind == more points)
    sorted_possible_cards = sorted([[item, value] for item, value in possible_cards.items()], key=lambda x: (x[1], card_priorities(x[0])))
    
    #fill the hand with the best possible cards
    while len(hand) < k:
        if sorted_possible_cards[0][1] <= 0:
            del sorted_possible_cards[0]
        hand += sorted_possible_cards[0][0]
        sorted_possible_cards[0][1] -= 1

    return "".join(sorted([c for c in hand], key= lambda x: card_priorities(x)))

if __name__ == "__main__":
    n, k = tuple(map(int, input().split()))

    played_cards = input()
    actions = [action == "y" for action in input()]

    print(main(n, k, played_cards, actions))
