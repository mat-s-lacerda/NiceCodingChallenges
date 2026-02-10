import uuid
from utils import NoMoneyException

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
        self.id: str = uuid.uuid4()
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


class Bank:
    """
    Represents a game bank.

    Parameters
    ----------

    Attributes
    ----------   
    ledger : dict
        A dictionary to keep track of bets and settlements.

    Methods
    -------
    receive_bet()
        Adds a bet to the bank.
    settle_round_result()
        Calculates the result of a round and updates the wallet accordingly.
    reset()
        Clears the ledger for a new round.

    Notes
    -----
    This class represents a game bank with a ledger for keeping track of bets and settlements.
    """

    def __init__(self):
        self.ledger: dict = {}

    def receive_bet(self, bet: int, wallet: Wallet):
        self.ledger[wallet.id] = bet
        print(f"Wallet {wallet.id} made a {bet} credits bet!")

    def settle_round_result(self, result: str, wallet: Wallet):
        debt: int = self.ledger.get(wallet.id, 0)

        match result:
            case "Win":
                total: int = debt * 2
                wallet.profit(total)
                print(f"You won {total} credits!")
            case "Lose":
                print("You lost your bet!")
            case "Push":
                wallet.profit(debt)
                print(f"You've received {debt} credits!")
            case "Blackjack":
                total: int = debt + int(debt*1.5)
                wallet.profit(total)
                print(f"You won {total}!")
        print(f"You current bankroll: {wallet.bankroll} credits")
    
    def reset(self):
        self.ledger: dict = {}


if __name__ == "__main__":
    bank: Bank = Bank()
    wallet: Wallet = Wallet()

    bet: int = wallet.bet()
    bank.receive_bet(bet=bet, wallet=wallet)

    bank.settle_round_result(result="Blackjack", wallet=wallet)
    
    bank.reset()
