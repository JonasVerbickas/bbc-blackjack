from enum import Enum

class PlayerStatus(Enum):
	"""A player status has a name and a value."""
	WON = 1
	BUSTED = 2
	STAND = 3

	def __str__(self):
		return f"{self.name}:{self.value}"

	def __repr__(self):
		return self.__str__()