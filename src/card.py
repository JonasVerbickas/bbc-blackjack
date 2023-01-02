from .suit import Suit
from .rank import Rank


class Card:
    """A card has a suit and a rank."""

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def get_value(self) -> int:
        return max(self.rank.value, 10)

    def __str__(self) -> str:
        return self.rank.name + " of " + self.suit.name

    def __repr__(self) -> str:
        return self.__str__()
