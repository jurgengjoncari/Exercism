codons_to_proteins = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine", 
    "UCC": "Serine", 
    "UCA": "Serine", 
    "UCG": "Serine",
    "UAU": "Tyrosine", 
    "UAC": "Tyrosine",
    "UGU": "Cysteine", 
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", 
    "UAG": "STOP", 
    "UGA": "STOP"
}
def proteins(strand):
    codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    proteins = []
    for codon in codons:
        if codons_to_proteins[codon] == "STOP":
            break
        proteins.append(codons_to_proteins[codon])
    return proteins