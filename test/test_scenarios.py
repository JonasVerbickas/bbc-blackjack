import unittest
from blackjack import BlackJack
from src.hand import Hand
from src.card import Card
from src.suit import Suit
from src.rank import Rank


class RankTestCase(unittest.TestCase):
    """Effectively integration testing"""

    def test_number_of_cards_in_opening_hand(self):
        self.game = BlackJack()
        self.game.deal_cards()
        self.assertEqual(len(self.game.player.hand.cards), 2)

    def test_hit(self):
        self.game = BlackJack()
        self.game.deal_cards()
        original_score = self.game.player.hand.value
        self.game.hit(self.game.player)
        self.assertEqual(len(self.game.player.hand.cards), 3)
        # self.assertGreater(self.game.player.hand.value, original_score)
        # intuitively, the score should be greater than the original score
        # but this is not the case
        # since ace can change to have value of 1
        # therefore the score can remain equal or even decrease
        # this is tested in test_hand.py

    def test_stand(self):
        # this test doesn't make sense with my implementation
        pass

    def test_value1(self):
        self.hand = Hand()
        self.hand.add_card(Card(Suit.CLUBS, Rank.KING))
        self.assertEqual(self.hand.value, 10)
        self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        self.assertEqual(self.hand.value, 21)

    def test_value2(self):
        self.hand = Hand()
        self.hand.add_card(Card(Suit.CLUBS, Rank.KING))
        self.assertEqual(self.hand.value, 10)
        self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        self.assertEqual(self.hand.value, 21)
        self.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        self.assertEqual(self.hand.value, 21)

    def test_value3(self):
        self.hand = Hand()
        self.hand.add_card(Card(Suit.CLUBS, Rank.NINE))
        self.assertEqual(self.hand.value, 9)
        self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        self.assertEqual(self.hand.value, 20)
        self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        self.assertEqual(self.hand.value, 21)
