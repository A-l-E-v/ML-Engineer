from hand import Hand

class Player:
    def __init__(self, chips=100):
        self.chips = chips
        self.bet = 0
        self.hand = Hand()

    def place_bet(self, amount):
        if amount <= self.chips:
            self.bet = amount
            return True
        return False

    def double_down(self):
        if self.chips >= self.bet:
            self.chips -= self.bet
            self.bet *= 2
            return True
        return False

    def reset(self):
        self.hand.clear()
        self.bet = 0
