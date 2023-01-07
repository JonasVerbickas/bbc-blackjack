import unittest
from src.suit import Suit


class SuitTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.suit = Suit

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_suits(self):
        """Test that there are 4 suits in a deck of cards."""
        number_of_suits = len(self.suit)
        self.assertEqual(number_of_suits, 4)
