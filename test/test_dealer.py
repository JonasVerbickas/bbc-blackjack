import unittest
from src.dealer import Dealer


class DealerTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.dealer = Dealer()

    def tearDown(self):  # this method will be run after each tests
        pass
