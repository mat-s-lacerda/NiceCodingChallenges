"""
Functions for playing blackjack. 
This module contains functions for dealing cards, checking for blackjack, and comparing hands.
"""

from hand import Hand, Card
from deck import Deck


def is_blackjack(hand: Hand) -> bool:
    """
    Verify if a hand is a blackjack, which is a hand with 21 points and only two cards.

    Parameters
    ----------
    hand : Hand
        The hand to be checked.

    Returns
    -------
    bool
        True if the hand is a blackjack, False otherwise.
    """

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
        

def deal_round(deck: Deck) -> tuple[Hand, Hand]:
    """
    Deal two cards to the player and one card (visible) to the dealer. 
    Then, check if either hand is a blackjack.

    Parameters
    ----------
    deck : Deck
        The deck of cards to deal from.

    Returns
    -------
    tuple[Hand, Hand]
        A tuple containing the player's hand and the dealer's hand.
    """
    from player import Gambler, Player

    gambler = Gambler()
    dealer = Player()

    gambler_hand: Hand = gambler.hand
    dealer_hand: Hand = dealer.hand

    for i in range(1,3):
        card: Card = deck.draw()
        gambler_hand.get_one_card(card)
        print(f"Player receives card {card}")


        card: Card = deck.draw()
        dealer_hand.get_one_card(card)
        
        if i != 1:
            print(f"Dealer receives a card")
            continue

        print(f"Dealer receives card {card}")

    gambler_hand.is_blackjack = is_blackjack(gambler_hand)
    dealer_hand.is_blackjack = is_blackjack(dealer_hand)

    hands: tuple[Hand, Hand] = (gambler_hand, dealer_hand)
     
    return hands


def player_turn(deck: Deck, player: Hand) -> str:
    """
    Simulate the player's turn. The player can choose to stand or hit, and the game ends if the player busts or chooses to stand.
    After each choice, the player's hand is printed.

    Parameters
    ----------
    deck : Deck
        The deck of cards to deal from.
    player : Hand
        The player's hand.

    Returns
    -------
    str
        A string indicating whether the player chose to stand or hit, and whether the player busts.
    """

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
    """
    Simulate the dealer's turn. The dealer not can choose, but it is verified if the dealer has 17 or more points.
    After each choice, the dealer's hand is printed.

    Parameters
    ----------
    deck : Deck
        The deck of cards to deal from.
    dealer : Hand
        The dealer's hand.

    Returns
    -------
    """

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
    """
    Compare the player's and dealer's hands to determine the result of the game.

    Parameters
    ----------
    player : Hand
        The player's hand.
    dealer : Hand
        The dealer's hand.

    Returns
    -------
    str
        A string indicating the result of the game, based on the player's and dealer's hands and the comparison of their totals.
    """
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

class NoMoneyException(Exception):
    pass

