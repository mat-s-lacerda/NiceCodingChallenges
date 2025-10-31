### Creating a Class Card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.rank_val_map = {
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
        self.suit = suit
        if suit not in ['♠','♥','♦','♣']:
            raise Exception('Invalid suit')

    @property
    def value(self):
        try: 
            value: int = self.rank_val_map[self.rank]
        except KeyError:
            raise KeyError('Invalid rank')
        return value
    
    def __repr__(self):
        card: str = self.rank + self.suit
        return card


a = Card('J', '♠')
print(a.value)
print(a)
