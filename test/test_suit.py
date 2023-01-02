import unittest
from src.suit import Suit

class SuitTestCase(unittest.TestCase):
	
		def setUp(self):  # this method will be run before each test
				self.suit = Suit

		def tearDown(self):  # this method will be run after each tests
				pass

		def test_number_of_cards(self):
				number_of_cards = len(self.suit)
				self.assertEqual(number_of_cards, 4)