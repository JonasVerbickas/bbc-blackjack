from .hand import Hand
from .player_choice import PlayerChoice
from .card import Card
from . import config 

class Player:
    def __init__(self, name: str):
        self.name = name
        self.balance = config.INITIAL_BALANCE
        self.bet = 0
        self.hand: Hand = None

    def ascii_list_of_cards(self, cards: list[Card]) -> list[str]:
        """
        Instead of a boring text version of the card we render an ASCII image of the card.
        Implementation taken from: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
        """
        # create an empty list of list, each sublist is a line
        lines = ["" for _ in range(7)]
        for index, card in enumerate(cards):
            space = '' if card.rank.value == 10 else ' ' 
            # add the individual card on a line by line basis
            lines[0] += ('┌─────────┐')
            lines[1] += ('│{}{}       │'.format(card.rank.short_unicode_repr(), space))  # use two {} one for char, one for space or char
            lines[2] += ('│         │')
            lines[3] += ('│    {}    │'.format(card.suit))
            lines[4] += ('│         │')
            lines[5] += ('│       {}{}│'.format(space, card.rank.short_unicode_repr()))
            lines[6] += ('└─────────┘')
        return lines
    
    def ascii_hand(self):
        return "\n".join(self.ascii_list_of_cards(self.hand.cards))
    
    def new_hand(self, hand: Hand) -> None:
        """Discards the old hand and receives a new one"""
        self.hand = hand
    
    def get_move(self) -> PlayerChoice:
        """Gets input from the player"""
        choice = None
        while choice not in [str(c.value) for c in PlayerChoice]:
            choice = input(f"Make a decision: {[str(c) for c in PlayerChoice]}: ")
        return PlayerChoice(int(choice))
    
    def get_bet(self):
        """Gets the bet from the player"""
        bet = None
        while bet is None or (bet > self.balance or bet < 0):
            try:
                bet = int(input(f"Your balance={self.balance} | Enter your bet: "))
            except ValueError:
                print("Please enter a number")
        self.bet = bet