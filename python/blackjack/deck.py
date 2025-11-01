from card import Card
from random import shuffle
class Deck:
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

    def set_deck(self):
        self.cards = self.create()
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


