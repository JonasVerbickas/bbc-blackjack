from .deck import Deck
from .hand import Hand
from .card import Card
from .player import Player
from .player_choice import PlayerChoice
from . import config


class Dealer(Player):
    """In my implementation Dealer is just another player that has infinite balance and a deck of cards"""

    def __init__(self):
        super().__init__("Dealer")
        self.balance = float("inf")
        self.deck = Deck()
        self.hide_card = True

    def deal_hand(self) -> Hand:
        """
        Deals a hand of config.INITIAL_HAND_SIZE cards
        """
        self.hide_card = True
        hand = Hand()
        for i in range(config.INITIAL_HAND_SIZE):
            hand.add_card(self.deal_card())
        return hand

    def _ascii_version_of_hidden_card(self, cards: list[Card]) -> list[str]:
        """
        Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over.
        Implementation taken from https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards.
        """
        # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
        lines = [
            "┌─────────┐",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "│░░░░░░░░░│",
            "└─────────┘",
        ]
        # store the non-flipped over card after the one that is flipped over
        cards_except_first = self._ascii_list_of_cards(cards[1:])
        for index, line in enumerate(cards_except_first):
            lines[index] += line
        return lines

    def ascii_hand(self) -> str:
        """
        @Overriden Player method.
        Returns different ascii art depending on whether the player is supposed to see the first card or not.
        """
        if self.hide_card:
            ascii_list_with_hidden = self._ascii_version_of_hidden_card(self.hand.cards)
        else:
            ascii_list_with_hidden = self._ascii_list_of_cards(self.hand.cards)
        return "\n".join(ascii_list_with_hidden)

    def deal_card(self) -> Card:
        return self.deck.deal_card()

    def get_move(self) -> PlayerChoice:
        """
        @Overriden Player method.
        Returns the move the dealer "wants to" make.
        Utilizes a constant for how much the dealer wants to hit.
        """
        self.hide_card = False
        if self.hand.value < config.DEALER_STAND_THRESHOLD:
            return PlayerChoice.HIT
        else:
            return PlayerChoice.STAND

    def get_visible_value(self) -> int:
        """
        Returns the value cards visible to the player.
        Assumes that only the first card is hidden.
        Should be extended to allow to hide more cards in the future.
        """
        # TODO
        # Make sure this works when different game configurations are implemented
        # e.g. more initial visible cards
        # to the point where total value is larger than BLACKJACK threshold
        # and aces have to use value of 1
        if self.hide_card:
            return self.hand.value - self.hand.cards[0].get_value()
        else:
            return self.hand.value

    def print_ascii_hand_with_score(self) -> None:
        """
        @Overriden Player method.
        Prints the ascii version of the dealer's hand and the score of the hand that the player can see.
        """
        print(self.ascii_hand())
        print(
            f"Cards held by the dealer are valued at {self.get_visible_value()} points"
        )
