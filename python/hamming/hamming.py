def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands should be of equal length.")
    
    count = 0
    for letter in range(len(strand_a)):
        if strand_a[letter] != strand_b[letter]:
            count += 1
    return count