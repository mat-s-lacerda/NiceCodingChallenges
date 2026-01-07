from economy import Wallet, Bank
from utils import NoMoneyException, deal_round, player_turn, dealer_turn, compare
from deck import Deck
from hand import Hand


def play_round():
    player_w: Wallet = Wallet()
    round_b: Bank = Bank()
    while True: 
        print(player_w.status())
        bet: int = int(input('How much do you want to bet? '))
        try:
            player_w.bet(bet)
        except NoMoneyException as e:
            print(str(e))
            continue
        round_b.receive_bet(bet,player_w)
        round_d: Deck = Deck()

        player: Hand
        dealer: Hand
        player, dealer = deal_round(round_d)

        player_turn(round_d, player)
        dealer_turn(round_d, dealer)
        result: str = compare(player, dealer)

        if result == "Win":
            player_w.profit(bet*2)
            print("Você ganhou!")
        elif result == "Blackjack":
            player_w.profit(bet+(bet*1.5))
            print("Você fez um Blackjack!")
        elif result == "Push":
            player_w.profit(bet)
            print("Você empatou!")
        else:
            print("Você perdeu mesmo!")

play_round()