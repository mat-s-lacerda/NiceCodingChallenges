from hand import Hand, Card
from deck import Deck

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

def deal_round(deck: Deck) -> tuple[Hand, Hand]:
    player = Hand()
    dealer = Hand()
    for i in range(1,3):
        player.get_one_card(deck.draw())
        dealer.get_one_card(deck.draw())
    tupla = (player, dealer)
     
    return tupla

print(deal_round(Deck()))