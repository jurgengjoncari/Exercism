def is_isogram(string):
    low_alnum = [c for c in string.lower() if c.isalnum()]
    return len(low_alnum) == len(set(low_alnum))