import uuid
from utils import NoMoneyException

class Wallet:
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


class Bank:
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
