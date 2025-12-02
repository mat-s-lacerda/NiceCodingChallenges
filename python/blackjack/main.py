from economy import Wallet, Bank
from utils import NoMoneyException, deal_round
from deck import Deck
from hand import Hand


def play_round():
    player_w: Wallet = Wallet()
    round_b: Bank = Bank()
    while True: 
        bet: int = int(input('How much do you want to bet? '))
        try:
            player_w.bet(bet)
        except NoMoneyException as e:
            print(str(e))
            break
        round_b.receive_bet(bet,player_w)
        round_d: Deck = Deck()

        player: Hand
        dealer: Hand
        player, dealer = deal_round(round_d)