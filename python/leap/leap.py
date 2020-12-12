def leap_year(year):
    # on every year that is evenly divisible by 4
    if not (year % 4 == 0 and year % 100 != 0 and year % 400 != 0):
        return False
    return True
