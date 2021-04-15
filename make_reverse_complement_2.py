class ReverComp:
    @staticmethod
    def reverse_seq(seq) -> str:
        reverse_seq = seq[::-1]
        return reverse_seq

    @staticmethod
    def make_G_complementary(nuc) -> str:
        if nuc == 'G':
            return 'C'
        else:
            raise ValueError(f"make_G_complementary received wrong nucleotide: {nuc}")

    @staticmethod
    def make_C_complementary(nuc) -> str:
        if nuc == 'C':
            return 'G'
        else:
            raise ValueError(f"make_C_complementary received wrong nucleotide: {nuc}")

    @staticmethod
    def make_A_complementary(nuc) -> str:
        if nuc == 'A':
            return 'T'
        else:
            raise ValueError(f"make_A_complementary received wrong nucleotide: {nuc}")

    @staticmethod
    def make_T_complementary(nuc) -> str:
        if nuc == 'T':
            return 'A'
        else:
            raise ValueError(f"make_T_complementary received wrong nucleotide: {nuc}")