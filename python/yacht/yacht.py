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

class yacht:
    # Score categories.
    # Change the values as you see fit.
    YACHT = 0
    ONES = 0
    TWOS = 0
    THREES = 0
    FOURS = 0
    FIVES = 0
    SIXES = 0
    FULL_HOUSE = 0
    FOUR_OF_A_KIND = 0
    LITTLE_STRAIGHT = 0
    BIG_STRAIGHT = 0
    CHOICE = 0

    def score(self, dice, category):
        self.dice = dice
        self.category = category
        if self.category == yacht.ONES:
            yacht.ONES += self.dice.count("1")
            return yacht.ONES