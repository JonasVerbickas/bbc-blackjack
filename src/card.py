from .suit import Suit
from .rank import Rank


class Card:
    """A card has a suit and a rank."""

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def get_value(self) -> int:
        # ace will be made to have value of 1 inside `hand.py`
        if self.rank == Rank.ACE:
            return 11
        else:
            return min(self.rank.value, 10)

    def __str__(self) -> str:
        return self.suit.short_unicode_repr() + self.rank.name 

    def __repr__(self) -> str:
        return self.__str__()
