from player import Gambler

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

    def receive_bet(self, bet: int, gambler: Gambler):
        self.ledger[gambler.id] = bet
        print(f"Wallet {gambler.id} made a {bet} credits bet!")

    def settle_round_result(self, result: str, gambler: Gambler):
        debt: int = self.ledger.get(gambler.id, 0)
        wallet: Wallet = gambler.wallet

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


#if __name__ == "__main__":
#    bank: Bank = Bank()
#    wallet: Wallet = Wallet()
#
#    bet: int = wallet.bet()
#    bank.receive_bet(bet=bet, wallet=wallet)
#
#    bank.settle_round_result(result="Blackjack", wallet=wallet)
#    
#    bank.reset()
