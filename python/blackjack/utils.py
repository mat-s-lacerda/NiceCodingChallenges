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

    player.is_blackjack = is_blackjack(player)
    dealer.is_blackjack = is_blackjack(dealer)

    hands: tuple[Hand, Hand] = (player, dealer)
     
    return hands



def player_turn(deck: Deck, player: Hand) -> str:
    print(f"Suas cartas são:{player} e a soma é:{player.total}")
    
    while True:
        choice = input("Deseja parar (s) ou pedir mais uma carta (h)?")
        if choice.lower() not in ('s', 'h'):
            raise ValueError(f'Invalid option!\nChoose "s" or "h".')
        match choice:
            case 's':
                print("Você é um frouxo!")
                return 'stand'
            case 'h':
                player.get_one_card(deck.draw())
                print(f"Agora suas cartas são:{player} e a soma é:{player.total}")
                if player.total > 21:
                    print("Bust, otário!")
                    player.is_bust = True
                    return 'bust'



def dealer_turn(deck: Deck, dealer: Hand) -> None:
    while True:
        print(f"As cartas do dealer são:{dealer} e a soma é:{dealer.total}")
        if dealer.total < 17:
            dealer.get_one_card(deck.draw())
        elif dealer.total <= 21:
            return 'stand'
        else:
            dealer.is_bust = True
            return 'bust'
          
def compare(player: Hand, dealer: Hand) -> str:
    # Finais imediatos
    if player.is_bust:
        return "Lose"
    if dealer.is_bust:
        return "Win"

    # Blackjacks
    if player.is_blackjack and dealer.is_blackjack:
        return "Push"
    if player.is_blackjack:
        return "Blackjack"
    if dealer.is_blackjack:
        return "Lose"

    # Pontuações "normais"
    if player.total == dealer.total:
        return "Push"
    return "Win" if player.total > dealer.total else "Lose"
    


deck = Deck()
player, dealer = deal_round(deck)
result_player = player_turn(deck,player)
result_dealer = dealer_turn(deck,dealer)
#print(result_dealer)
result_game = compare(player, dealer)
print(result_game)
