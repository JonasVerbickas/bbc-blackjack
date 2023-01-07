from enum import Enum


class Suit(Enum):
    """Even though suit doesn't matter in score calculation I use it to visuallize the hand."""

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def short_unicode_repr(self) -> str:
        """
        To make the hand more readable I use unicode symbols to represent the suit.
        (it also helps if a reduce the amount of printed text whenever debugging lists of cards)
        """
        map_to_unicode = "♠♦♥♣"
        return map_to_unicode[self.value-1]

    def __str__(self) -> str:
        return self.short_unicode_repr()

    def __repr__(self) -> str:
        return self.__str__()

