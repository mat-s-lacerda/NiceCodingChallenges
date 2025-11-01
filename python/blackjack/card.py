### Creating a Class Card
#import logging
from typing import Literal

class Card:
    """
    This class represents a playing card
    
    # Variables:
        RANKS: dict[str, int] -> All the possible ranks for a card and its corresponding values
        SUITS: list[str] -> All the possible card's suits
    
    # Args:
        rank: Literal -> The Card's rank
        suit: Literal -> The Card's suit
    
    # Properties:
        value: int -> The Card's value

    """
    RANKS: dict[str, int] = {
        'A':11, 
        '2':2, 
        '3':3, 
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
        'K':10,
        'Q':10,
        'J':10
    }
    SUITS: list[str] = ['♠','♥','♦','♣']

    def __init__(
            self, 
            rank: Literal['A','2','3','4','5','6','7','8','9','10','J','Q','K'], 
            suit: Literal['♠','♥','♦','♣']
        ):
        self.rank: str = rank
        self.suit: str = suit
        if suit not in self.SUITS:
            raise ValueError(f'Invalid suit!\nChoose one of {",".join(self.SUITS)}')

    @property
    def value(self):
        try: 
            value: int = self.RANKS[self.rank]
        except KeyError:
            raise ValueError(f'Invalid rank!\nChoose one of {",".join([key for key in self.RANKS.keys()])}')
        return value
    
    def __repr__(self):
        card: str = self.rank + self.suit
        return card

if __name__ == '__main__':
    print(Card.RANKS)
    a: Card = Card('J', '♠')
    print(a.RANKS)
    print(type(a))
