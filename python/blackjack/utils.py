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
        card: Card = deck.draw()
        player.get_one_card(card)
        print(f"Player receives card {card}")


        card: Card = deck.draw()
        dealer.get_one_card(card)
        
        if i != 1:
            print(f"Dealer receives a card")
            continue

        print(f"Dealer receives card {card}")

    hands: tuple[Hand, Hand] = (player, dealer)
     
    return hands

deal_round(Deck())
