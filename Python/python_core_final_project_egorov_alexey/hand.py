from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            if card.rank == 'A':
                aces += 1
            value += card.value

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def is_blackjack(self):
        return len(self.cards) == 2 and self.calculate_value() == 21

    def is_bust(self):
        return self.calculate_value() > 21

    def clear(self):
        self.cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
