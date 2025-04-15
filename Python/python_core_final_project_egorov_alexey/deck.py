import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in Card.SUITS
                      for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None
