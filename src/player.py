from .hand import Hand
from .player_choice import PlayerChoice

class Player:
	def __init__(self, name: str):
		self.name = name
		self.bankroll = 100
		self.bet = 0
		self.hand: Hand = None
	
	def new_hand(self, hand: Hand) -> None:
		"""Discards the old hand and receives a new one"""
		self.hand = hand
	
	def get_input(self) -> PlayerChoice:
		"""Gets input from the player"""
		choice = None
		while choice not in [str(c.value) for c in PlayerChoice]:
			choice = input(f"Make a decision: {[str(c) for c in PlayerChoice]}: ")
		return PlayerChoice(int(choice))