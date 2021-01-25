def is_isogram(string):
    low_alnum = ''.join(s for s in string.lower() if s.isalnum())
    for c in low_alnum:
        if low_alnum.count(c) != 1:
            return False
    return True
