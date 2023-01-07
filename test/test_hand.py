import unittest
from src.hand import Hand, AceStatus
from src.card import Card
from src.rank import Rank
from src.suit import Suit


class HandTestCase(unittest.TestCase):
    """
    !!=====WARNING=====!!
    These tests were designed with regular blackjack rules in mind.
    Altering the blackjack rules may cause these tests to fail
    e.g. changing the threshold for a blackjack to be something other than 21.
    """

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

    def test_hard_going_past_21(self):
        """
        Test if hand value goes past 21 when ace is hard
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
        self.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
        self.assertEqual(self.hand.value, 20)
        self.assertEqual(self.hand.ace_status, AceStatus.HARD)
        self.hand.add_card(Card(Suit.CLUBS, Rank.TWO))
        self.assertEqual(self.hand.value, 22)
        self.assertEqual(self.hand.ace_status, AceStatus.HARD)

    def test_no_ace(self):
        """
        If there is no ace in hand its value should go past 21
        """
        self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
        self.hand.add_card(Card(Suit.CLUBS, Rank.TEN))
        self.assertEqual(self.hand.value, 10)
        self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
        self.hand.add_card(Card(Suit.CLUBS, Rank.NINE))
        self.assertEqual(self.hand.value, 10 + 9)
        self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)
        self.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
        self.assertEqual(self.hand.value, 10 + 9 + 8)
        self.assertEqual(self.hand.ace_status, AceStatus.NO_ACE)

    def test_many_aces(self):
        """
        Test that ace value is 1 when hand goes past 21
        """
        self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        self.assertEqual(self.hand.value, 11)
        expected_value = 12
        for i in range(20):
            self.hand.add_card(Card(Suit.CLUBS, Rank.ACE))
            self.assertEqual(self.hand.value, expected_value + i)
            self.assertEqual(self.hand.ace_status, AceStatus.HARD)
