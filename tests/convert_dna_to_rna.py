from script import convert_dna_to_rna
import unittest


class MyTestCase(unittest.TestCase):
    def test_convert_dna_to_rna(self):
        '''Test case for a function to convert DNA sequesnce into RNA sequence'''
        self.assertEqual(convert_dna_to_rna("ATTTGGCTACTAACAATCTA"), "AUUUGGCUACUAACAAUCUA")
        self.assertEqual(convert_dna_to_rna("GTTGTAATGGCCTACATTA"), "GUUGUAAUGGCCUACAUUA")
        self.assertEqual(convert_dna_to_rna("CAGGTGGTGTTGTTCAGTT"), "CAGGUGGUGUUGUUCAGUU")
        self.assertEqual(convert_dna_to_rna("GCTAACTAAC"), "GCUAACUAAC")
        self.assertEqual(convert_dna_to_rna("GCTAACTAACATCTTTGGCACTGTT"), "GCUAACUAACAUCUUUGGCACUGUU")
        self.assertEqual(convert_dna_to_rna("TATGAAAAACTCAAA"), "UAUGAAAAACUCAAA")
        self.assertEqual(convert_dna_to_rna("CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"), "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU")


if __name__ == '__main__':
    unittest.main()
