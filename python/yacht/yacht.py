YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: x.count(1)
TWOS = lambda x: 2 * x.count(2)
THREES = lambda x: 3 * x.count(3)
FOURS = lambda x: 4 * x.count(4)
FIVES = lambda x: 5 * x.count(5)
SIXES = lambda x: 6 * x.count(6)
FULL_HOUSE = lambda x: full_house(x)
FOUR_OF_A_KIND = lambda x: four_of_a_kind(x)
LITTLE_STRAIGHT = lambda x: 30 if set(x) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda x: 30 if set(x) == {2, 3, 4, 5, 6} else 0
CHOICE = sum


def full_house(dice):
    if len(set(dice)) == 2:
        for number in set(dice):
            if dice.count(number) == 2 or dice.count(number) == 3:
                return sum(dice)
    return 0


def four_of_a_kind(dice):
    if len(set(dice)) <= 2:
        for number in set(dice):
            if dice.count(number) >= 4:
                return 4 * number
    return 0


def score(dice, category):
    return category(dice)
