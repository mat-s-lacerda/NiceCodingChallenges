from card import Card
class Deck:
    def __init__(
        self
    ):
        self.cards: list[Card] = [] 
        for suit in Card.SUITS:
            for rank in Card.RANKS.keys():
                card: Card = Card(rank=rank,suit=suit)
                self.cards.append(card)
            


a = Deck()
print(a.cards)


