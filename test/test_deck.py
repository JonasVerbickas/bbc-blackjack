import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_deal(self):
        card = self.deck.deal_card()
        self.assertEqual(len(self.deck.cards), 51)
        self.assertEqual(card.__class__.__name__, "Card")


if __name__ == "__main__":
    unittest.main()
