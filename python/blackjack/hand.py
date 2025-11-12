from card import Card

class Hand:

    def __init__(self):
        self.cards_by_rank: dict[str, list[Card]] = {}
        self.total: int = 0
        self.is_bust: bool = False
        self.is_blackjack: bool = False

    def get_one_card(self, card: Card):
        cards: list[Card] = self.cards_by_rank.get(card.rank, [])
        cards.append(card)
        self.cards_by_rank[card.rank] = cards

        self.total += card.value

        if self.total > 21:
            self.account_for_aces()
    
    def account_for_aces(self) -> None:
        try:
            aces: list[Card] = self.cards_by_rank['A']
        except KeyError:
            print("No aces found in Hand")
            return
        
        for ace in aces:
            if self.total <= 21:
                return
            if not ace.use_alt_val:
                self.total -= ace.value
                ace.use_alt_val = True
                self.total += ace.value
            
        print("No Aces to Account for")

    def __repr__(self):
        cards = []
        for value in self.cards_by_rank.values():
            cards.extend(value)
        return str(cards)
                