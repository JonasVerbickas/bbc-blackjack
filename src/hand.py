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
    
    def ascii_version_of_card(self, cards: list[Card], return_string=True):
        """
        Instead of a boring text version of the card we render an ASCII image of the card.
        :param cards: One or more card objects
        :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
        keep it as a list so that the dealer can add a hidden card in front of the list
        """
        # create an empty list of list, each sublist is a line
        lines = ["" for _ in range(7)]

        for index, card in enumerate(cards):
            space = '' if card.rank.value == 10 else " " 
            # add the individual card on a line by line basis
            lines[0] += ('┌─────────┐')
            lines[1] += ('│{}{}       │'.format(card.rank.short_unicode_repr(), space))  # use two {} one for char, one for space or char
            lines[2] += ('│         │')
            lines[3] += ('│    {}    │'.format(card.suit))
            lines[4] += ('│         │')
            lines[5] += ('│       {}{}│'.format(space, card.rank.short_unicode_repr()))
            lines[6] += ('└─────────┘')

        # hidden cards do not use string
        if return_string:
            return '\n'.join(lines)
        else:
            return lines

    
    def __str__(self):
        str_column_of_cards = self.ascii_version_of_card(self.cards) #''.join([c.__repr__() for c in self.cards])
        return f"\n{str_column_of_cards} valued at {self.value}"
    
    def __repr__(self) -> str:
        return self.__str__()