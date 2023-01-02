import unittest
from src.rank import Rank

class RankTestCase(unittest.TestCase):
	
		def setUp(self):  # this method will be run before each test
				self.rank = Rank

		def tearDown(self):  # this method will be run after each tests
				pass

		def test_number_of_cards(self):
				number_of_cards = len(self.rank)
				self.assertEqual(number_of_cards, 13)