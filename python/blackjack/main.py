"""
Main module for playing blackjack.
This module orchestrates the entire game flow, including betting, dealing cards, player and dealer turns, and settling the results using the Bank and Wallet systems.
"""

from economy import Bank
from utils import NoMoneyException, deal_round, player_turn, dealer_turn, compare
from deck import Deck
from hand import Hand
from player import Wallet


def play_round():
    """
    This function plays a single round of blackjack. It contains the main game loop, with importants functions from other modules, like deal_round, player_turn, dealer_turn, compare and the Wallet.

    Parameters
    ----------

    Returns
    -------

    Notes
    -----
    - The game continues indefinitely until the user manually stops it
      (pressing 'Ctrl+C').
    - It handles 'NoMoneyException' to prevent betting more than the
      available bankroll.
    """

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