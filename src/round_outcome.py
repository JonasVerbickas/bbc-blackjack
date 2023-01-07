from enum import Enum


class RoundOutcome(Enum):
    """A player status has a name and a value."""

    BLACKJACK = 0
    PLAYER_WON = 1
    DEALER_WON = 2
    TIE = 3

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
