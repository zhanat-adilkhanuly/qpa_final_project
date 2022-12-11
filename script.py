import sqlite3
import matplotlib.pyplot as plt
from Bio import SeqIO

CODON = 3
DATABASE = 'data/first_database.db'


def convert_dna_to_rna(dna_sequence: str) -> str:
    '''Converts DNA sequence in string into RNA sequence in string'''
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    rna_sequence: str = ''
    for nucleotide in dna_sequence:
        cursor.execute(f"""SELECT RNA_NUCLEOTIDE FROM DNA_BASES WHERE DNA_NUCLEOTIDE = '{nucleotide}'""")
        corr_rna_nucleotide = cursor.fetchall()[0][0]
        rna_sequence += corr_rna_nucleotide

    cursor.close()

    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    '''Converts RNA sequence in string into Amino Acids(that add up to protein) in string'''
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    protein: str = ''
    index = 0

    while True:
        if len(rna_sequence) < CODON:
            return
        if (index + 2) < len(rna_sequence):
            nucl_1 = rna_sequence[index]
            nucl_2 = rna_sequence[index + 1]
            nucl_3 = rna_sequence[index + 2]
            cursor.execute(f"""SELECT AMINO_ACID FROM AMINO_ACIDS WHERE FIRST_NUCLEOTIDE = '{nucl_1}' """
                           f""" AND SECOND_NUCLEOTIDE = '{nucl_2}' AND THIRD_NUCLEOTIDE = '{nucl_3}'""")
            protein += cursor.fetchall()[0][0]
            index = index + 3
        else:
            break

    cursor.close()
    return protein


def gc_content_ratio(dna_sequence: str) -> int:
    '''Helper function of Task 3. to calculate GC content of any sequence'''
    return round((dna_sequence.count("C") + dna_sequence.count("G"))
                 / len(dna_sequence) * 100)


def read_fasta(path) -> str:
    '''Helper function of Task 3. to read a sequence in fasta format and change it into a string sequence'''
    genome = SeqIO.read(path, "fasta")
    dna_sequence = str(genome.seq)
    return dna_sequence


def gc_ratio_plot(dna_sequence: str, step=100):
    '''
    Task 3. Divides the sequence into several subsequence with step nucleotides in each
    and plots the gc-content-ratio vs. genome position graph
    and saves it in data directory
    '''

    dna_subsequenced = []
    for i in range(0, len(dna_sequence) - step + 1, step):
        subsequence = dna_sequence[i:i + step]
        dna_subsequenced.append(gc_content_ratio(subsequence))

    plt.plot(dna_subsequenced)
    plt.xlabel("Genome position")
    plt.ylabel("GC-content(%)")
    plt.title("GC-content distribution")
    plt.show()
    #plt.savefig("data/gc_content_ratio_sars_cov_2.png")


if __name__ == "__main__":
    dna_sequence = read_fasta('data/dna_sequence.fna')
    gc_ratio_plot(dna_sequence)
