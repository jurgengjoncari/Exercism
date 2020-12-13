complements = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
    }
def to_rna(dna_strand):
    return ''.join([complements[nucleotide] for nucleotide in dna_strand])