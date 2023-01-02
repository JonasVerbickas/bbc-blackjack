from .suit import Suit
from .rank import Rank
from .card import Card
import random


class Deck:
    """A deck has a list of cards and can deal a card."""
    def __init__(self):
        self.cards = self.generate_shuffled_list_of_cards()

    @staticmethod
    def generate_shuffled_list_of_cards():
        cards = []
        for s in Suit:
            for r in Rank:
                card = Card(s, r)
                cards.append(card)
        print("Before shuffle", cards)
        random.shuffle(cards)
        print("After shuffle", cards)
        return cards
    
    def deal(self):
        return self.cards.pop()
