from player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__(chips=0)  # У дилера неограниченные фишки

    def should_hit(self):
        return self.hand.calculate_value() < 17
