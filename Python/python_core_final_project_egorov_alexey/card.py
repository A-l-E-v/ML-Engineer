class Card:
    SUITS = ('♣', '♦', '♥', '♠')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    @property
    def value(self):
        if self.rank in ('J', 'Q', 'K'):
            return 10
        if self.rank == 'A':
            return 11  # Базовое значение, корректируется в Hand
        return int(self.rank)
