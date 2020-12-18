from math import sqrt
def score(x, y):
    """ The outer circle has a radius of 10 units,
    the middle circle a radius of 5 units, and 
    the inner circle a radius of 1. 
    """

    radius = sqrt(x ** 2 + y ** 2)

    # If the dart lands in the inner circle of the target, player earns 10 points.
    if radius <= 1:
        return 10
    # If the dart lands in the middle circle of the target, player earns 5 points.
    elif radius <= 5:
        return 5
    # If the dart lands in the outer circle of the target, player earns 1 point.
    elif radius <= 10:
        return 1
    # If the dart lands outside the target, player earns no points (0 points).
    else:
        return 0
