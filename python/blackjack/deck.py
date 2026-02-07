from card import Card
from random import shuffle
class Deck:
    """
    Represents a deck of playing cards.

    Parameters
    ----------

    Attributes
    ----------
    
    cards: list[Card]
        A list of cards in the deck.

    Methods
    -------
    create()
        Creates a deck of cards.
    shuffle()
        Shuffles the deck of cards.
    draw()
        Draws a card from the deck.

    Notes
    -----
    This class creates a deck of 52 cards, shuffles it, and provides a method to draw a card. 
    If the deck runs out of cards, it creates a new deck.
    """

    def __init__(
        self
    ):
        self.set_deck()

    def create(self):
        cards: list[Card] = [] 
        for suit in Card.SUITS:
            for rank in Card.RANKS.keys():
                card: Card = Card(rank=rank,suit=suit)
                cards.append(card)
        return cards

    def shuffle(self):
        shuffle(self.cards)

    def set_deck(self, cards: list[Card] = None):
        self.cards: list[Card] = self.create() if not cards else cards
        self.shuffle()

    def draw(self):
        if len(self.cards) <= 10:
            self.set_deck()
        card: Card = self.cards.pop()
        return card

    

#a = Deck()
#while True:
#    print(len(a.cards))
#    a.draw()


