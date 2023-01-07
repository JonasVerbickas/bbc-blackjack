"""
Hyperparameters to configure the game and possibly use custom rules.
Values for cards can be changed in Card.get_value() method or in Rank enum.
"""
DEALER_STAND_THRESHOLD = 17
BLACKJACK = 21
INITIAL_BALANCE = 100
NUMBER_OF_ROUNDS = 5
BLACKJACK_MULTIPLIER = 1.5
MIN_BET = 10 # please keep it positive
INITIAL_HAND_SIZE = 2