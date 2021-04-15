import unittest
from make_reverse_complement_2 import ReverComp

class test_rc_converting_skills(unittest.TestCase):
    def setUp(self) -> None:
        self.rever_comp = ReverComp()

    def test_if_seq_gets_reversed(self):
        # Assume
        sequence = 'ATGCGCTAC'
        # Action
        reversed_seq = self.rever_comp.reverse_seq(seq=sequence)
        # Assert
        self.assertEqual(reversed_seq, 'CATCGCGTA')

    def test_if_G_complementation_works_with_arg(self):
        # Assume
        nucleotide = 'G'
        # Action
        complementary_nucleotide = self.rever_comp.make_G_complementary(nuc=nucleotide)
        # Assert
        self.assertEqual(complementary_nucleotide, 'C')

    def test_if_G_complementation_raise_value_error_by_passing_down_wrong_nucleotide(self):
        # Assume
        wrong_nucleotide = 'A'
        # Action & Assert
        with self.assertRaises(ValueError):
            self.rever_comp.make_G_complementary(nuc=wrong_nucleotide)

    def test_if_C_complementation_works_with_arg(self):
        # Assume
        nucleotide = 'C'
        # Action
        complementary_nucleotide = self.rever_comp.make_C_complementary(nuc=nucleotide)
        # Assert
        self.assertEqual(complementary_nucleotide, 'G')

    def test_if_C_complementation_raise_value_error_by_passing_down_wrong_nucleotide(self):
        # Assume
        wrong_nucleotide = 'A'
        # Action & Assert
        with self.assertRaises(ValueError):
            self.rever_comp.make_C_complementary(nuc=wrong_nucleotide)

    def test_if_A_complementation_works_with_arg(self):
        # Assume
        nucleotide = 'A'
        # Action
        complementary_nucleotide = self.rever_comp.make_A_complementary(nuc=nucleotide)
        # Assert
        self.assertEqual(complementary_nucleotide, 'T')

    def test_if_A_complementation_raise_value_error_by_passing_down_wrong_nucleotide(self):
        # Assume
        wrong_nucleotide = 'G'
        # Action & Assert
        with self.assertRaises(ValueError):
            self.rever_comp.make_A_complementary(nuc=wrong_nucleotide)

    def test_if_T_complementation_works_with_arg(self):
        # Assume
        nucleotide = 'T'
        # Action
        complementary_nucleotide = self.rever_comp.make_T_complementary(nuc=nucleotide)
        # Assert
        self.assertEqual(complementary_nucleotide, 'A')

    def test_if_T_complementation_raise_value_error_by_passing_down_wrong_nucleotide(self):
        # Assume
        wrong_nucleotide = 'G'
        # Action & Assert
        with self.assertRaises(ValueError):
            self.rever_comp.make_T_complementary(nuc=wrong_nucleotide)