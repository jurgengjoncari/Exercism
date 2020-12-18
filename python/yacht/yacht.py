"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    # if category == YACHT:
        
    if category == ONES:
        return dice.count(1)
    if category == TWOS:
        return 2 * dice.count(2)
    if category == THREES:
        return 3 * dice.count(3)
    if category == FOURS:
        return 4 * dice.count(4)
    if category == FIVES:
        return 5 * dice.count(5)
    if category == SIXES:
        return 6 * dice.count(6)
    if category == FULL_HOUSE:
        
    if category == FOUR_OF_A_KIND:
        
    if category == LITTLE_STRAIGHT:
        
    if category == BIG_STRAIGHT:
        
    if category == CHOICE:
        
