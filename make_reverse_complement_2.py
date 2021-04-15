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
            raise ValueError(f"make_G_complementary received false nucleotide: {nuc}")
