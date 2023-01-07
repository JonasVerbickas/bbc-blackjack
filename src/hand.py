from .card import Card
from .rank import Rank
from enum import Enum
from . import config

class AceStatus(Enum):
    """
    Used to describe the status of the ace in a hand and allow for according score adjustments.
    """
    NO_ACE = 1
    SOFT = 2
    HARD = 3

class Hand:
    def __init__(self):
        self.dealt = False
        self.cards: list[Card] = []
        self.ace_status = AceStatus.NO_ACE
        self.value = 0
    
    def add_card(self, card: Card):
        """
        Append a card to the hand and adjust the value of the hand accordingly.
        """
        self.value += card.get_value()
        if card.rank == Rank.ACE:
            self.ace_status = AceStatus.SOFT
        if self.ace_status == AceStatus.SOFT and self.value > config.BLACKJACK:
            self.value -= 10
            self.ace_status = AceStatus.HARD
        self.cards.append(card)
    
    def __str__(self):
        str_column_of_cards = ''.join([c.__repr__() for c in self.cards])
        return f"\n{str_column_of_cards} valued at {self.value}"
    
    def __repr__(self) -> str:
        return self.__str__()
