from data import description


def convert_dna_to_rna(dna_sequence: str) -> str:
    rna_sequence: str = ''
    for nucleotide in dna_sequence:
        corr_nucleotide = description.dna_to_rna[nucleotide]
        rna_sequence += corr_nucleotide
    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    protein: str = ''
    index = 0

    while True:
        if len(rna_sequence) < 3:
            return
        if (index + 2) < len(rna_sequence):
            nucl_1 = rna_sequence[index]
            nucl_2 = rna_sequence[index+1]
            nucl_3 = rna_sequence[index+2]
            protein += description.rna_to_protein[nucl_1][nucl_2][nucl_3]
            index = index + 3
        else:
            break

    return protein
