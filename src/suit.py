from enum import Enum


class Suit(Enum):
    """A suit has a name and a value."""

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
