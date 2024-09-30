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

    if (not possible_cards or len(certain_cards) > k
    or any(val <= 0 for val in possible_cards.values()) or
    sum((val for val in possible_cards.values())) < k - len(certain_cards)): # if there aren't enough possible cards or a card has had 4+ y
        return "impossible"

    hand = "".join((card for card in certain_cards))
    for card in hand:
        if card in possible_cards:
            possible_cards[card] -= 1 # remove certain cards from possible 
            
    # sort by seen most (closer to 4 of a kind == more points)
    possible_cards = dict(filter(lambda x: possible_cards[x[0]] > 0, possible_cards.items()))
    if not possible_cards:
        return "impossible"
    
    # small hack to solve edge cases
    if len(hand) + 8 == k:
        min_lex_card = min(possible_cards, key=lambda x: card_priorities(x))
        hand += min_lex_card * possible_cards[min_lex_card]
        del possible_cards[min_lex_card]
        
        min_lex_card = min(possible_cards, key=lambda x: card_priorities(x))
        hand += min_lex_card * possible_cards[min_lex_card]
        del possible_cards[min_lex_card]
        
        if len(hand) == k:
            return "".join(sorted([c for c in hand], key= lambda x: card_priorities(x)))
        
    #fill the hand with the best possible cards
    while len(hand) < k:
        if not possible_cards:
            return "impossible"
        card = min(possible_cards, key=lambda x: (possible_cards[x], card_priorities(x)))
        hand += card
        possible_cards[card] -= 1
        possible_cards = dict(filter(lambda x: possible_cards[x[0]] > 0, possible_cards.items()))

    return "".join(sorted([c for c in hand], key= lambda x: card_priorities(x)))

if __name__ == "__main__":
    n, k = tuple(map(int, input().split()))

    played_cards = input()
    actions = [action == "y" for action in input()]
    print(main(n, k, played_cards, actions))
