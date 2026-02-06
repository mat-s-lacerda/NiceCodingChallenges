### Creating a Class Card
#import logging
from typing import Literal

class Card:
    """
    Represents a playing card.

    Parameters
    ----------
    rank : str
        The card's rank (e.g., 'A', '2', 'K').
    suit : str
        The card's suit (e.g., '♠', '♥').

    Attributes
    ----------
    RANKS : dict
        Dictionary containing all possible ranks and their corresponding values.
    SUITS : list
        List containing all possible card suits.

    Notes
    -----
    The `value` property returns the card's numerical value based on its rank.
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
