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
    RANKS: dict[str, tuple[int, int]] = {
        'A':(11,1), 
        '2':(2,None), 
        '3':(3,None), 
        '4':(4,None),
        '5':(5,None),
        '6':(6,None),
        '7':(7,None),
        '8':(8,None),
        '9':(9,None),
        '10':(10,None),
        'K':(10,None),
        'Q':(10,None),
        'J':(10,None)
    }
    SUITS: list[str] = ['♠','♥','♦','♣']

    def __init__(
            self, 
            rank: Literal['A','2','3','4','5','6','7','8','9','10','J','Q','K'], 
            suit: Literal['♠','♥','♦','♣']
        ):
        self.rank: str = rank
        self.suit: str = suit
        self.use_alt_val: bool = False
        if suit not in self.SUITS:
            raise ValueError(f'Invalid suit!\nChoose one of {",".join(self.SUITS)}')

    @property
    def value(self) -> int:
        try: 
            value, alt = self.RANKS[self.rank]
        except KeyError:
            raise ValueError(f'Invalid rank!\nChoose one of {",".join([key for key in self.RANKS.keys()])}')
        return value if not self.use_alt_val else alt
    
    def __repr__(self):
        card: str = self.rank + self.suit
        return card

if __name__ == '__main__':
    print(Card.RANKS)
    a: Card = Card('A', '♠')
    print(a.RANKS)
    print(type(a))
    print(a.alt)
