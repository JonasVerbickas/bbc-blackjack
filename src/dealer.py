from .deck import Deck
from .hand import Hand
from .card import Card
from .player import Player
from .player_choice import PlayerChoice
from .config import DEALER_STAND_THRESHOLD


class Dealer(Player):
    """In my implementation Dealer is just another player that has infinite balance and a deck of cards"""

    def __init__(self):
        super().__init__("Dealer")
        self.balance = float('inf')
        self.deck = Deck()
        self.hide_card = True

    def deal_hand(self):
        """Deals a hand of 2 cards"""
        self.hide_card = True
        hand = Hand()
        hand.add_card(self.deal_card())
        hand.add_card(self.deal_card())
        return hand

    def ascii_version_of_hidden_card(self, cards: list[Card]):
        """
        Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over.
        Implementation taken from https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards.
        """
        # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
        lines = ['┌─────────┐', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│',  '└─────────┘']
        # store the non-flipped over card after the one that is flipped over
        cards_except_first = self.ascii_list_of_cards(cards[1:])
        for index, line in enumerate(cards_except_first):
            lines[index]+=(line)
        return lines

    def ascii_hand(self) -> str:
        if self.hide_card:
            ascii_list_with_hidden = self.ascii_version_of_hidden_card(self.hand.cards)
        else:
            ascii_list_with_hidden = self.ascii_list_of_cards(self.hand.cards)
        return "\n".join(ascii_list_with_hidden)
    
    def deal_card(self) -> Card:
        return self.deck.deal_card()
    
    def get_move(self) -> PlayerChoice:
        self.hide_card = False
        if self.hand.value < DEALER_STAND_THRESHOLD:
            return PlayerChoice.HIT
        else:
            return PlayerChoice.STAND
    
    def __str__(self):
        return f"Dealer has {len(self.deck)} cards left in the deck"