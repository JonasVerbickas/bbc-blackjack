from src.dealer import Dealer
from src.player import Player
from src.card import Card
from src.player_choice import PlayerChoice
from src.round_outcome import RoundOutcome
import src.config as config
import time
import os


class BlackJack:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player("Player 1")
    
    def hit(self, player: Player) -> Card:
        """
        Allows the player to hit 
        """
        dealt_card = self.dealer.deal_card()
        print(f"{player.name} hits and gets {dealt_card}")
        player.hand.add_card(dealt_card)
        return dealt_card
    
    def allow_to_hit(self, player: Player) -> int:
        """
        Allows the player to hit until they stand or bust
        """
        # 1. allow player to hit until they stand or bust
        while player.hand.value < config.BLACKJACK and player.get_move() == PlayerChoice.HIT:
            self.hit(self.player)
            # sleep for 0.5 seconds if dealer is hitting for a dramatic effect
            if player.__class__.__name__ == "Dealer":
                time.sleep(0.5)
            self.draw_board()
        return player.hand.value
    
    def draw_board(self):
        """
        Use to create stable visual representation of the game board.
        That clears the screen before drawing the board.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player.print_ascii_hand_with_score()
        print("="*50)
        self.dealer.print_ascii_hand_with_score()
        print(f"Player's bet: {self.player.bet}")
    
    def deal_cards(self):
        """
        Deals the initial cards to the dealer and player.
        """
        self.dealer.set_hand(self.dealer.deal_hand())
        self.player.set_hand(self.dealer.deal_hand())
 
    def play_round(self):
        """
        Plays a round of blackjack by collecting the bet and allowing the player to hit until they stand or bust.
        """
        # 0. Collect bet
        self.player.get_bet()
        # 1. Initialize hands
        self.deal_cards()
        self.draw_board()
        # 2. Check if player has blackjack 
        if self.player.hand.value == config.BLACKJACK:
            if self.player.hand.value == self.dealer.hand.value:
                return RoundOutcome.TIE
            else:
                return RoundOutcome.BLACKJACK
        # 3. If not, allow player to hit until they stand or bust
        self.allow_to_hit(self.player)
        # 4. If player busts, dealer wins
        if self.player.hand.value > config.BLACKJACK:
            return RoundOutcome.DEALER_WON
        # 5. If player stands, allow dealer to hit until they stand or bust
        self.allow_to_hit(self.dealer)
        # 6. If dealer busts, player wins
        if self.dealer.hand.value > config.BLACKJACK:
            return RoundOutcome.PLAYER_WON
        # 7. If dealer stands, compare hands and determine winner
        if self.dealer.hand.value > self.player.hand.value:
            return RoundOutcome.DEALER_WON
        elif self.dealer.hand.value < self.player.hand.value:
            return RoundOutcome.PLAYER_WON
        else:
            return RoundOutcome.TIE
    
    def update_player_balance(self, outcome: RoundOutcome):
        """
        Updates the player's bank based on the outcome of the round
        """
        if outcome == RoundOutcome.BLACKJACK:
            self.player.balance += int(self.player.bet * config.BLACKJACK_MULTIPLIER)
        elif outcome == RoundOutcome.PLAYER_WON:
            self.player.balance += self.player.bet
        elif outcome == RoundOutcome.DEALER_WON:
            self.player.balance -= self.player.bet
        else:
            pass

def play():
    """
    Plays multiple rounds of blackjack
    """
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
