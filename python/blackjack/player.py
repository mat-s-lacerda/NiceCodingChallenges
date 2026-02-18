from hand import Hand
import uuid
from utils import NoMoneyException

class Player:

    def __init__(self):
        self.id: str = uuid.uuid4()
        self.hand: Hand = Hand()


class Gambler(Player):
    
    def __init__(self, bankroll: int = 100, base_bet: int = 10, **kwargs):
        super().__init__(**kwargs)
        self.wallet: Wallet = Wallet(bankroll=bankroll, base_bet=base_bet)

class Wallet:
    """
    Represents a playing wallet.

    Parameters
    ----------
    bankroll : int
        Represents the wallet's current balance.
    base_bet : int
        Represents the base bet amount for the wallet.    

    Attributes
    ----------
    id : uuid
        Represents the wallet's unique identifier.
    bankroll : int
        Represents the wallet's current balance.
    base_bet : int
        Represents the base bet amount for the wallet. 

    Methods
    -------
    bet()
        Makes a bet from the wallet.
    profit()
        Adds money to the wallet.
    status()
        Returns the wallet's current balance.

    Notes
    -----
    This class represents a playing wallet, with a unique identifier, a current balance, and a base bet amount. 
    If no base bet is provided, it defaults to 10. If the wallet runs out of money, it raises a NoMoneyException.
    """

    def __init__(self, bankroll: int = 100, base_bet: int = 10):
        self.bankroll: int = bankroll
        self.base_bet: int = base_bet
    
    def bet(self, ammount: int = None) -> int:
        ammount: int = ammount if ammount else self.base_bet 
        
        if self.bankroll < ammount:
            raise NoMoneyException(f"Not enough in wallet to bet! You only have {self.bankroll} credits left.")
         
        self.bankroll -= ammount
        return ammount

    def profit(self, ammount: int):
        self.bankroll += ammount

    def status(self):
        return self.bankroll
    
    

#teste = Gambler()
#print(teste.wallet.bankroll)