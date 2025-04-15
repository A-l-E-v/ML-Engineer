import sys
from deck import Deck
from player import Player
from dealer import Dealer

sys.stdout.reconfigure(encoding='utf-8')

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.log_file = 'blackjacklog.txt'

    def log(self, message):
        print(message)
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(message + '\n')

    def get_bet(self):
        while True:
            try:
                bet = int(input("\nPLAYER'S BET: "))
                if bet > 0 and self.player.place_bet(bet):
                    return bet
                self.log("Error: Bet must be positive integer within available chips")
            except ValueError:
                self.log("Error: Invalid input. Please enter a number")

    def display_hands(self, final=False):
        print(f"\nPlayer's hand: {self.player.hand} ({self.player.hand.calculate_value()})")
        if final:
            print(f"Dealer's hand: {self.dealer.hand} ({self.dealer.hand.calculate_value()})")
        else:
            print(f"Dealer's hand: {self.dealer.hand.cards[0]}, [hidden]")

    def player_turn(self):
        while True:
            action = input("PLAYER'S MOVE (hit/stand/double): ").strip().lower()

            if action in ('hit', 'h'):
                self.player.hand.add_card(self.deck.deal_card())
                self.display_hands()
                if self.player.hand.is_bust():
                    return False

            elif action in ('stand', 's'):
                return True

            elif action in ('double', 'd', 'dd'):
                if len(self.player.hand.cards) == 2:
                    if self.player.double_down():
                        self.player.hand.add_card(self.deck.deal_card())
                        self.display_hands()
                        return False  # После double автоматически stand
                    else:
                        self.log("Error: Not enough chips to double down")
                else:
                    self.log("Error: Can only double down on first two cards")

            else:
                self.log("Error: Invalid move. Choose hit/stand/double")

    def dealer_turn(self):
        while self.dealer.should_hit():
            self.dealer.hand.add_card(self.deck.deal_card())
            self.display_hands(final=True)  # Отображаем карты дилера после каждого хода

    def determine_winner(self):
        player_value = self.player.hand.calculate_value()
        dealer_value = self.dealer.hand.calculate_value()

        if self.player.hand.is_blackjack() and self.dealer.hand.is_blackjack():
            return "push"
        if self.player.hand.is_blackjack():
            return "blackjack"
        if player_value > 21:
            return "bust"
        if dealer_value > 21:
            return "dealer_bust"
        if player_value > dealer_value:
            return "win"
        if dealer_value > player_value:
            return "lose"
        return "push"

    def play_round(self):
        # Сброс рук перед началом нового раунда
        self.player.reset()
        self.dealer.reset()

        # 1. Ввод ставки
        if not self.get_bet():
            self.log("Error: Not enough chips to place a bet")
            return

        # 2. Сначала обычная раздача
        self.player.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())

        # 3. Показать карты
        self.display_hands()

        # 4. Проверить блэкджек
        if self.player.hand.is_blackjack():
            self.display_result("blackjack")
            return

        # 5. Ход игрока
        if not self.player_turn():
            self.display_result("bust")
            return

        # 6. Ход дилера
        self.dealer_turn()

        # 7. Определить победителя
        result = self.determine_winner()
        self.display_hands(final=True)
        self.display_result(result)

    def start(self):
        self.log("\n♣♦♥♠ Welcome to Blackjack! ♣♦♥♠")
        while True:
            if self.player.chips <= 0:
                self.log("Game over: No more chips")
                break
            self.play_round()
            play_again = input("Play again? (y/n): ").lower()
            if play_again != 'y':
                break

    def display_result(self, result):
        player_value = self.player.hand.calculate_value()
        dealer_value = self.dealer.hand.calculate_value()

        result_message = "\n♣♦♥♠ Game finish ♣♦♥♠\nRESULTS:\n"
        result_message += f"___player: {player_value}"
        result_message += " (blackjack)" if self.player.hand.is_blackjack() else ""
        result_message += " (bust)" if self.player.hand.is_bust() else ""

        result_message += f"\n___dealer: {dealer_value}"
        result_message += " (blackjack)" if self.dealer.hand.is_blackjack() else ""
        result_message += " (bust)" if self.dealer.hand.is_bust() else ""

        # Определяем исход игры
        if result == "blackjack":
            self.player.chips += int(self.player.bet * 1.5)
            result_message += "\n___player won (blackjack)"
        elif result == "bust":
            result_message += "\n___player lost (bust)"
        elif result == "dealer_bust":
            self.player.chips += self.player.bet * 2
            result_message += "\n___player won (dealer bust)"
        elif result == "win":
            self.player.chips += self.player.bet * 2
            result_message += "\n___player won"
        elif result == "lose":
            result_message += "\n___player lost"
        else:  # push
            self.player.chips += self.player.bet
            result_message += "\n___draw"

        self.log(result_message)
        self.log(f"Player's chips: {self.player.chips}")

if __name__ == "__main__":
    game = Game()
    game.start()
