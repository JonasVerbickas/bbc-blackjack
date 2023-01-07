from .card import Card
from .rank import Rank
from enum import Enum

class AceStatus(Enum):
    NO_ACE = 0
    SOFT = 1
    HARD = 2

class Hand:
    def __init__(self):
        self.dealt = False
        self.cards: list[Card] = []
        self.ace_status = AceStatus.NO_ACE
        self.value = 0
    
    def add_card(self, card: Card):
        self.value += card.get_value()
        if card.rank == Rank.ACE:
            self.ace_status = AceStatus.SOFT
        if self.ace_status == AceStatus.SOFT and self.value > 21:
            self.value -= 10
            self.ace_status = AceStatus.HARD
        self.cards.append(card)
    
    def __str__(self):
        return f"{self.cards} valued at {self.value}"
    
    def __repr__(self) -> str:
        return self.__str__()