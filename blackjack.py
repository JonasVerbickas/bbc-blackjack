from src.dealer import Dealer
from src.player import Player
from src.player_choice import PlayerChoice
from src.player_status import PlayerStatus

class BlackJack:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player("Player 1")
        
    def allow_to_hit(self, player: Player) -> int:
        """Allows the player to hit until they stand or bust"""
        while player.get_input() == PlayerChoice.HIT and player.hand.value < 21:
            dealt_card = self.dealer.deal_card()
            print(f"{player.name} hits and gets {dealt_card}")
            player.hand.add_card(dealt_card)
            print(f"Now {player.name} has {player.hand}")
        return player.hand.value
    
    def eval_standing(self, player: Player):
        """Evaluates the standing of the player"""
        if player.hand.value > 21:
            print(f"{player.name} busts")
            return PlayerStatus.BUSTED
        elif player.hand.value == 21:
            print(f"{player.name} wins")
            return PlayerStatus.WON
        else:
            print(f"{player.name} stands")
            return PlayerStatus.STAND
 
    def play_round(self):
        """Plays a round of blackjack"""
        self.dealer.new_hand(self.dealer.deal_hand())
        self.player.new_hand(self.dealer.deal_hand())
        print("Player hand: ", self.player.hand)
        print("Dealer hand: ", self.dealer.hand)
        self.allow_to_hit(self.player)
        self.eval_standing(self.player)

        if self.player.hand.value > 21:
            print("Player busts")
        elif self.player.hand.value == 21:
            print("Player wins")
        else:
            print("Player stands")
            self.allow_to_hit(self.dealer)
            if self.dealer.hand.value > 21:
                print("Dealer busts")
            elif self.dealer.hand.value == 21:
                print("Dealer wins")
            else:
                print("Dealer stands")
                if self.dealer.hand.value > self.player.hand.value:
                    print("Dealer wins")
                else:
                    print("Player wins")


def play():
    """Plays a game of blackjack"""
    game = BlackJack()
    game.play_round()

if __name__ == '__main__':
    play()
