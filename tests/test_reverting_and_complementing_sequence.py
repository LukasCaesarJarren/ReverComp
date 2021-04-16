import unittest
from make_reverse_complement_2 import ReverComp

class test_rc_converting_skills(unittest.TestCase):


    def test_if_seq_gets_reversed(self):
        # Assume
        sequence = 'ATGCGCTAC'
        rever_comp = ReverComp()
        # Action
        reversed_seq = rever_comp.reverse_seq(seq=sequence)
        # Assert
        self.assertEqual(reversed_seq, 'CATCGCGTA')

    def test_if_sequences_rc_lst_gets_complementary_of_G_appended(self):
        # Assume
        nucleotide = 'G'
        rever_comp = ReverComp()
        # Action
        rever_comp.append_complementary_of_G_to_seq_rc_lst(nuc=nucleotide)
        sequences_rc_lst = rever_comp.lst_of_sequences_rc
        # Assert
        self.assertEqual(sequences_rc_lst, ['C'])

    def test_if_sequences_rc_lst_gets_complementary_of_C_appended(self):
        # Assume
        nucleotide = 'C'
        rever_comp = ReverComp()
        # Action
        rever_comp.append_complementary_of_C_to_seq_rc_lst(nuc=nucleotide)
        sequences_rc_lst = rever_comp.lst_of_sequences_rc
        # Assert
        self.assertEqual(sequences_rc_lst, ['G'])

    def test_if_sequences_rc_lst_gets_complementary_of_A_appended(self):
        # Assume
        nucleotide = 'A'
        rever_comp = ReverComp()
        # Action
        rever_comp.append_complementary_of_A_to_seq_rc_lst(nuc=nucleotide)
        sequences_rc_lst = rever_comp.lst_of_sequences_rc
        # Assert
        self.assertEqual(sequences_rc_lst, ['T'])

    def test_if_sequences_rc_lst_gets_complementary_of_T_appended(self):
        # Assume
        nucleotide = 'T'
        rever_comp = ReverComp()
        # Action
        rever_comp.append_complementary_of_T_to_seq_rc_lst(nuc=nucleotide)
        sequences_rc_lst = rever_comp.lst_of_sequences_rc
        # Assert
        self.assertEqual(sequences_rc_lst, ['A'])

    def test_if_sequences_rc_lst_is_instanciated_by_calling_ReverComp(self):
        # Assume
        rever_comp = ReverComp()
        lst_of_sequences_rc = rever_comp.lst_of_sequences_rc
        # Action
        length_of_seq_rc_lst = len(lst_of_sequences_rc)
        # Assert
        self.assertEqual(length_of_seq_rc_lst, 0)

    def test_if_rc_sequence_get_joined_correct_together(self):
        # Assume
        rever_comp = ReverComp()
        DNA_sequence = ['A', 'T', 'G', 'G', 'C']
        # Action
        DNA_sequence_joined = rever_comp.join_lst_seq_rc(seq_as_lst=DNA_sequence)
        # Assert
        self.assertEqual(DNA_sequence_joined, 'ATGGC')

    def test_rc_functionality(self):
        # Assume
        rever_comp = ReverComp()
        seq_before_rc_conversion = 'ATGGTCAG'
        # Action
        seq_after_rc_conversion = rever_comp.make_rc_conversion(seq_to_convert=seq_before_rc_conversion)
        # Assert
        self.assertEqual(seq_after_rc_conversion, 'CTGACCAT')

