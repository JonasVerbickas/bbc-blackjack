from enum import Enum


class PlayerChoice(Enum):
    """A player choice has a name and a value."""

    HIT = 1
    STAND = 2

    def __str__(self):
        return f"{self.name}:{self.value}"

    def __repr__(self):
        return self.__str__()
