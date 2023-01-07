from .deck import Deck
from .hand import Hand
from .card import Card
from .player import Player
from .player_choice import PlayerChoice
from .config import DEALER_STAND_THRESHOLD


class Dealer(Player):
	"""In my implementation Dealer is just another player that has infinite bankroll and a deck of cards"""

	def __init__(self):
		super().__init__("Dealer")
		self.bankroll = float('inf')
		self.deck = Deck()

	def deal_hand(self):
		"""Deals a hand of 2 cards"""
		hand = Hand()
		hand.add_card(self.deal_card())
		hand.add_card(self.deal_card())
		return hand
	
	def deal_card(self) -> Card:
		return self.deck.deal_card()
	
	def get_input(self) -> PlayerChoice:
		if self.hand.value < DEALER_STAND_THRESHOLD:
			return PlayerChoice.HIT
		else:
			return PlayerChoice.STAND
	
	def __str__(self):
		return f"Dealer has {len(self.deck)} cards left in the deck"