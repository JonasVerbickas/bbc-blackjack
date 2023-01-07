from src.dealer import Dealer
from src.player import Player
from src.player_choice import PlayerChoice
import src.config as config
from enum import Enum
import time
import os

class RoundOutcome(Enum):
    """A player status has a name and a value."""
    BLACKJACK = 0
    PLAYER_WON = 1
    DEALER_WON = 2
    TIE = 3

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class BlackJack:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player("Player 1")

    def allow_to_hit(self, player: Player) -> int:
        """Allows the player to hit until they stand or bust"""
        # 1. allow player to hit until they stand or bust
        while player.hand.value < config.BLACKJACK and player.get_move() == PlayerChoice.HIT:
            dealt_card = self.dealer.deal_card()
            print(f"{player.name} hits and gets {dealt_card}")
            player.hand.add_card(dealt_card)
            # sleep for 0.5 seconds if dealer is hitting for a dramatic effect
            if player.__class__.__name__ == "Dealer":
                time.sleep(0.5)
            self.draw_board()
        return player.hand.value
    
    def draw_board(self):
        """Draws the board"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Player's hand:\n{self.player.ascii_hand()}")
        print(f"Dealer's hand:\n{self.dealer.ascii_hand()}")
        print(f"Player's bet: {self.player.bet}")
 
    def play_round(self):
        """Plays a round of blackjack"""
        self.player.get_bet()
        # 0. Initialize hands
        self.dealer.new_hand(self.dealer.deal_hand())
        self.player.new_hand(self.dealer.deal_hand())
        self.draw_board()
        # 1. Check if player has blackjack 
        if self.player.hand.value == config.BLACKJACK:
            if self.player.hand.value == self.dealer.hand.value:
                return RoundOutcome.TIE
            else:
                return RoundOutcome.BLACKJACK

        # 2. If not, allow player to hit until they stand or bust
        self.allow_to_hit(self.player)

        # 3. If player busts, dealer wins
        if self.player.hand.value > config.BLACKJACK:
            return RoundOutcome.DEALER_WON

        # 4. If player stands, allow dealer to hit until they stand or bust
        self.allow_to_hit(self.dealer)

        # 5. If dealer busts, player wins
        if self.dealer.hand.value > config.BLACKJACK:
            return RoundOutcome.PLAYER_WON
        
        # 6. If dealer stands, compare hands and determine winner
        if self.dealer.hand.value > self.player.hand.value:
            return RoundOutcome.DEALER_WON
        elif self.dealer.hand.value < self.player.hand.value:
            return RoundOutcome.PLAYER_WON
        else:
            return RoundOutcome.TIE
    
    def update_player_balance(self, outcome: RoundOutcome):
        """Updates the player's bank based on the outcome of the round"""
        if outcome == RoundOutcome.BLACKJACK:
            self.player.balance += int(self.player.bet * config.BLACKJACK_MULTIPLIER)
        elif outcome == RoundOutcome.PLAYER_WON:
            self.player.balance += self.player.bet
        elif outcome == RoundOutcome.DEALER_WON:
            self.player.balance -= self.player.bet
        else:
            pass

def play():
    """Plays a game of blackjack"""
    game = BlackJack()
    for _ in range(config.NUMBER_OF_ROUNDS):
        outcome = game.play_round()
        print(outcome)
        game.update_player_balance(outcome)
        print("New player's balance: ", game.player.balance)
        if game.player.balance <= 0:
            print("You're out of money!")
            print("Game over!")
            break


if __name__ == '__main__':
    play()
