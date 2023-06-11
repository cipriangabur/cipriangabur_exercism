def to_rna(dna_strand):
    return "".join(["C" if dna == "G" else
                    "G" if dna == "C" else
                    "A" if dna == "T" else
                    "U" if dna == "A" else
                    dna for dna in dna_strand])
