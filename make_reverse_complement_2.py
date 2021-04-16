class ReverComp:
    def __init__(self):
        self.lst_of_sequences_rc = []

    def append_complementary_of_G_to_seq_rc_lst(self, nuc) -> None:
        if nuc == 'G':
            self.lst_of_sequences_rc.append('C')

    def append_complementary_of_C_to_seq_rc_lst(self, nuc) -> None:
        if nuc == 'C':
            self.lst_of_sequences_rc.append('G')

    def append_complementary_of_A_to_seq_rc_lst(self, nuc) -> None:
        if nuc == 'A':
            self.lst_of_sequences_rc.append('T')

    def append_complementary_of_T_to_seq_rc_lst(self, nuc) -> None:
        if nuc == 'T':
            self.lst_of_sequences_rc.append('A')

    def make_rc_conversion(self, seq_to_convert) -> str:
        reversed_seq = self.reverse_seq(seq=seq_to_convert)
        for nuc in reversed_seq:
            # elif better?
            self.append_complementary_of_A_to_seq_rc_lst(nuc=nuc)
            self.append_complementary_of_C_to_seq_rc_lst(nuc=nuc)
            self.append_complementary_of_G_to_seq_rc_lst(nuc=nuc)
            self.append_complementary_of_T_to_seq_rc_lst(nuc=nuc)
        seq_rc = self.join_lst_seq_rc(seq_as_lst=self.lst_of_sequences_rc)

        return seq_rc
    @staticmethod
    def join_lst_seq_rc(seq_as_lst) -> str:
        return ''.join(seq_as_lst)

    @staticmethod
    def reverse_seq(seq) -> str:
        reverse_seq = seq[::-1]
        return reverse_seq
