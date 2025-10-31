### Creating a Class Card
import logging
from typing import Literal

class Card:
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
    a: Card = Card('J', '♠')
    logging.info(a.value)
    logging.info(a)
