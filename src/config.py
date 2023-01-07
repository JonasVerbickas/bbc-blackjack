"""
Hyperparameters to configure the game and possibly use custom rules.
Values for cards can be changed in Card.get_value() method or in Rank enum.
"""
DEALER_STAND_THRESHOLD = 17
INITIAL_BALANCE = 100
NUMBER_OF_ROUNDS = 5
BLACKJACK_MULTIPLIER = 1.5
MIN_BET = 10  # please keep it positive

# these require changes in the code
# or might cause issues with the test suite
# so please don't change them!
# I could implement them, but the exam period is coming up and I need to revise :)
INITIAL_HAND_SIZE = 2
BLACKJACK = 21
