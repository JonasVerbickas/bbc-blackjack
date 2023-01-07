from enum import Enum


class Rank(Enum):
    """A rank has a name and a value."""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def short_unicode_repr(self) -> str:
        """Used to display the card using ascii art."""
        if self == Rank.ACE:
            return 'A'
        elif self == Rank.JACK:
            return 'J'
        elif self == Rank.QUEEN:
            return 'Q'
        elif self == Rank.KING:
            return 'K'
        else:
            return str(self.value)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
