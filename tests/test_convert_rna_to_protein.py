from script import convert_rna_to_protein
import unittest


class MyTestCase(unittest.TestCase):
    def test_convert_rna_to_protein(self):
        '''Test case for a function to convert RNA sequesnce into protein'''
        self.assertEqual(convert_rna_to_protein("AUUUGGCUACUAACAAUCUA"), "IWLLTI")
        self.assertEqual(convert_rna_to_protein("GUUGUAAUGGCCUACAUUA"), "VVMAYI")
        self.assertEqual(convert_rna_to_protein("CAGGUGGUGUUGUUCAGUU"), "QVVLFS")
        self.assertEqual(convert_rna_to_protein("GCUAACUAAC"), "AN.")
        self.assertEqual(convert_rna_to_protein("GCUAACUAACAUCUUUGGCACUGUU"), "AN.HLWHC")
        self.assertEqual(convert_rna_to_protein("UAUGAAAAACUCAAA"), "YEKLK")
        self.assertEqual(convert_rna_to_protein("CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"), "PVLDWLEEKF")


if __name__ == '__main__':
    unittest.main()