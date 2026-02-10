from card import Card

class Hand:
    """
    Represents a playing hand.

    Parameters
    ----------  

    Attributes
    ----------
    cards_by_rank : dict[str, list[Card]]
        A dictionary to store cards by rank.
    total : int
        The current total value of all cards inthe hand.
    is_bust : bool
        A flag indicating whether the hand is bust, which means the total value exceeds 21.
    is_blackjack : bool
        A flag indicating whether the hand is a blackjack, which means the total value is exactly 21.

    Methods
    -------
    get_one_card(card: Card)
        Adds a card to the hand and updates the total value. This method also checks for aces.
    account_for_aces()
        Adjusts the total value of the hand based on aces to prevent bust.

    Notes
    -----
    This class represents a playing hand with a dictionary to store cards by rank, a total value, and flags for bust and blackjack.
    
    """

    def __init__(self):
        self.cards_by_rank: dict[str, list[Card]] = {}
        self.total: int = 0
        self.is_bust: bool = False
        self.is_blackjack: bool = False

    def get_one_card(self, card: Card):
        cards: list[Card] = self.cards_by_rank.get(card.rank, [])
        cards.append(card)
        self.cards_by_rank[card.rank] = cards

        self.total += card.value

        if self.total > 21:
            self.account_for_aces()
    
    def account_for_aces(self) -> None:
        try:
            aces: list[Card] = self.cards_by_rank['A']
        except KeyError:
            print("No aces found in Hand")
            return
        
        for ace in aces:
            if self.total <= 21:
                return
            if not ace.use_alt_val:
                self.total -= ace.value
                ace.use_alt_val = True
                self.total += ace.value
            
        print("No Aces to Account for")

    def __repr__(self):
        cards = []
        for value in self.cards_by_rank.values():
            cards.extend(value)
        return str(cards)
                