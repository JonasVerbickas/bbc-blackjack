from enum import Enum


class Suit(Enum):
    """Even though suit doesn't matter in score calculation I use it to visuallize the hand."""

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
