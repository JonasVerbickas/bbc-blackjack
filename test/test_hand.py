import unittest
from src.hand import Hand, AceStatus
from src.card import Card
from src.rank import Rank
from src.suit import Suit

class HandTestCase(unittest.TestCase):
	
	def setUp(self):  # this method will be run before each test
		self.hand = Hand()

	def tearDown(self):  # this method will be run after each tests
		pass

	def test_soft_ace(self):
		"""
		Check if Ace status is changed to SOFT after it is added to hand
		"""
		self.hand.add_card(Card(Suit.CLUBS, Rank.TWO))
		self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.assertEqual(self.hand.value, 13)
		self.assertEqual(self.hand.ace_status, AceStatus.SOFT)
	
	def test_hard_ace(self):
		"""
		Test if ACE is converted to be worth 1 if hand value goes over 21
		It should flip the ace_status to HARD as well
		"""
		self.hand.add_card(Card(Suit.CLUBS, Rank.NINE))
		self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.assertEqual(self.hand.ace_status, AceStatus.SOFT)
		self.assertEqual(self.hand.value, 20)
		self.assertEqual(self.hand.ace_status, AceStatus.SOFT)
		self.hand.add_card(Card(Suit.CLUBS, Rank.TWO))
		self.assertEqual(self.hand.value, 12)
		self.assertEqual(self.hand.ace_status, AceStatus.HARD)
	
	def test_no_ace(self):
		"""
		If there is no ace in hand its value should go past 21
		"""
		self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
		self.hand.add_card(Card(Suit.CLUBS, Rank.TEN))
		self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
		self.hand.add_card(Card(Suit.CLUBS, Rank.NINE))
		self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
		self.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
		self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
		self.assertEqual(self.hand.value, 10+9+8)
	
	def test_two_aces(self):
		"""
		Test if two aces are added to hand
		"""
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.assertEqual(self.hand.value, 12)
		self.assertEqual(self.hand.ace_status, AceStatus.HARD)

	def test_three_aces(self):
		"""
		Test if three aces are added to hand
		"""
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
		self.assertEqual(self.hand.value, 13)
		self.assertEqual(self.hand.ace_status, AceStatus.HARD)