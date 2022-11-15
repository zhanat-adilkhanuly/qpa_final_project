import sqlite3


def convert_dna_to_rna(dna_sequence: str) -> str:
    conn = sqlite3.connect('data/first_database.db')
    cursor = conn.cursor()

    rna_sequence: str = ''
    for nucleotide in dna_sequence:
        cursor.execute(f"""SELECT RNA_NUCLEOTIDE FROM DNA_BASES WHERE DNA_NUCLEOTIDE = '{nucleotide}'""")
        corr_rna_nucleotide = cursor.fetchall()[0][0]
        rna_sequence += corr_rna_nucleotide

    cursor.close()

    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    conn = sqlite3.connect('data/first_database.db')
    cursor = conn.cursor()


    protein: str = ''
    index = 0

    while True:
        if len(rna_sequence) < 3:
            return
        if (index + 2) < len(rna_sequence):
            nucl_1 = rna_sequence[index]
            nucl_2 = rna_sequence[index+1]
            nucl_3 = rna_sequence[index+2]
            cursor.execute(f"""SELECT AMINO_ACID FROM AMINO_ACIDS WHERE FIRST_NUCLEOTIDE = '{nucl_1}' """
                            f""" AND SECOND_NUCLEOTIDE = '{nucl_2}' AND THIRD_NUCLEOTIDE = '{nucl_3}'""")
            protein += cursor.fetchall()[0][0]
            index = index + 3
        else:
            break

    cursor.close()
    return protein

#print(convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'))