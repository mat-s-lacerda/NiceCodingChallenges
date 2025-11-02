from hand import Hand, Card

def is_blackjack(hand: Hand) -> bool:
    if len(hand.cards_by_rank.keys()) == 1:
        return False
    
    total: int = 0
    for val in hand.cards_by_rank.values():

        card: Card = val[0]
        value: int = card.value
        total += value

    if total != 21:
        return False
    
    return True
        

#a = Hand()
#a.cards_by_rank = {
#    'A':[
#        Card('A', '♠')
#    ],
#    'K':[
#        Card('2', '♠')
#    ]
#}
#
#print(is_blackjack(a))